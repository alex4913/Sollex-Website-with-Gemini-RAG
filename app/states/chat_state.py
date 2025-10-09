import reflex as rx
import os
import google.generativeai as genai
import logging
from typing import TypedDict
import asyncio

vector_store: dict[str, list[float]] = {}
try:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
except Exception as e:
    logging.exception(f"Error configuring Google AI: {e}")


class Message(TypedDict):
    text: str
    is_user: bool


class ChatState(rx.State):
    """Manages the chat conversation and RAG logic."""

    messages: list[Message] = [
        {
            "text": "The information provided by Minerva is for general legal information only and does not constitute legal advice. No attorney-client relationship is created by using this service.",
            "is_user": False,
        },
        {
            "text": "I am Minerva, the AI assistant for the Law Office of Alexander S. Chang. How may I help you answer your preliminary questions?",
            "is_user": False,
        },
    ]
    is_typing: bool = False
    tos_accepted: bool = False
    scrolled_to_bottom: bool = False
    prompts: list[str] = [
        "Can a landlord evict a tenant without a court order?",
        "What is the economic loss doctrine in Utah contract law?",
        "What is the difference between Chapter 7 and Chapter 13 bankruptcy?",
    ]
    current_prompt_index: int = 0
    question_input: str = ""
    is_cycling_prompts: bool = False
    legal_docs: list[str] = [
        "The Law Office of Alexander S. Chang is a modern, AI-powered law firm.",
        "The firm was founded by Alexander S. Chang, an expert in generative artificial intelligence and its use in law.",
        "We offer a 'Modest Means Program' to provide affordable legal services to lower and middle-income individuals.",
        "Our Modest Means Program uses a tiered fee structure based on the Federal Poverty Guidelines, in collaboration with the Utah State Bar's Access to Justice section.",
        "Tier 1 serves clients with incomes between 125% and 300% of the Federal Poverty limit with flat fees and reduced hourly rates.",
        "Tier 2 serves clients with incomes between 300% and 500% of the Federal Poverty limit with competitive flat fees.",
        "Alexander S. Chang has published articles in the Utah Bar Journal on AI in legal practice and on asset protection trusts.",
    ]

    @rx.var
    def current_prompt_text(self) -> str:
        """The raw text of the current prompt."""
        if not self.prompts:
            return ""
        return self.prompts[self.current_prompt_index]

    @rx.var
    def current_prompt_display(self) -> str:
        """The current placeholder prompt to display with hint."""
        if not self.prompts:
            return "Ask your question here..."
        return f"{self.current_prompt_text} →[Tab]"

    @rx.event
    def handle_key_down(self, key: str):
        """Handle key down events in the input."""
        if key == "Tab":
            self.question_input = self.current_prompt_text
            return rx.call_script("event.preventDefault();")

    @rx.event
    def accept_tos(self):
        """Sets the terms of service as accepted."""
        self.tos_accepted = True

    @rx.event
    def set_scrolled_to_bottom(self):
        """Sets that the user has scrolled to the bottom of the TOS."""
        self.scrolled_to_bottom = True

    @rx.event
    def handle_tos_scroll(self):
        """Checks if the user has scrolled to the bottom of the TOS."""
        return rx.call_script("""
            const el = document.getElementById('tos-scroll-area');
            if (el) {
                const isAtBottom = el.scrollTop + el.clientHeight >= el.scrollHeight - 20;
                if (isAtBottom) {
                    __reflex_process_event({name: "chat_state.set_scrolled_to_bottom"});
                }
            }
            """)

    async def _create_embeddings(self):
        """Helper to pre-compute embeddings for the legal documents."""
        if not vector_store and self.legal_docs:
            print("Creating embeddings for documents...")
            try:
                response = await genai.embed_content_async(
                    model="models/text-embedding-004", content=self.legal_docs
                )
                for i, embedding in enumerate(response["embedding"]):
                    vector_store[self.legal_docs[i]] = embedding
                print("Embeddings created successfully.")
            except Exception as e:
                logging.exception(f"Error creating embeddings: {e}")

    @rx.event(background=True)
    async def cycle_prompts(self):
        """Cycles through placeholder prompts in the background."""
        while self.is_cycling_prompts:
            async with self:
                self.current_prompt_index = (self.current_prompt_index + 1) % len(
                    self.prompts
                )
            await asyncio.sleep(4)

    @rx.event
    async def minerva_page_load(self):
        """Event handler for when the Minerva page loads."""
        await self._create_embeddings()
        if not self.is_cycling_prompts:
            self.is_cycling_prompts = True
            return ChatState.cycle_prompts

    def _find_relevant_docs(self, query_embedding: list[float], top_k=2) -> list[str]:
        """Finds the most relevant documents from the vector store."""
        if not vector_store:
            return []
        import numpy as np

        similarities = []
        for doc, doc_embedding in vector_store.items():
            similarity = np.dot(query_embedding, doc_embedding) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(doc_embedding)
            )
            similarities.append((similarity, doc))
        similarities.sort(key=lambda x: x[0], reverse=True)
        return [doc for _, doc in similarities[:top_k]]

    @rx.event
    async def process_question(self, form_data: dict):
        """Processes the user's question, runs RAG, and gets a response."""
        question = form_data.get("question", "").strip()
        if not question or self.is_typing:
            return
        self.is_typing = True
        self.messages.append({"text": question, "is_user": True})
        self.messages.append({"text": "", "is_user": False})
        self.question_input = ""
        yield
        try:
            query_embedding_response = await genai.embed_content_async(
                model="models/text-embedding-004", content=question
            )
            query_embedding = query_embedding_response["embedding"]
            relevant_docs = self._find_relevant_docs(query_embedding)
            context = "".join(relevant_docs)
            model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
            prompt = f"You are a professional, helpful AI assistant for a solo practice law firm. Your tone should be trustworthy and modern. Answer the user's question based on the following context. If the context does not contain the answer, state that you do not have enough information but can schedule a consultation. Do not mention that you are using 'context'.\n\nContext:\n{context}\n\nQuestion:\n{question}\n\nAnswer:"
            stream = await model.generate_content_async(prompt, stream=True)
            current_text = ""
            async for chunk in stream:
                if chunk.text:
                    current_text += chunk.text
                    self.messages[-1]["text"] = current_text
                    yield
        except Exception as e:
            logging.exception(f"An error occurred: {e}")
            self.messages[-1]["text"] = f"An error occurred: {e}"
        finally:
            self.is_typing = False
            yield
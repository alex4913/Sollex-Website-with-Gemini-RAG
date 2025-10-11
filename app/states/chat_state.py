import reflex as rx
import os
import google.generativeai as genai
import logging
from typing import TypedDict, Any
import asyncio
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.retrievers import BaseRetriever

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
            "text": "The information provided by UCAP is for general legal information only and does not constitute legal advice. Do not submit or send any confidential or personal information. No attorney-client relationship is created by using UCAP.",
            "is_user": False,
        },
        {
            "text": "I am Minerva, the AI assistant for the Law Office of Alexander S. Chang. How may I help you answer your preliminary questions?",
            "is_user": False,
        },
    ]
    is_typing: bool = False
    tos_accepted: bool = False
    prompts: list[str] = [
        "Can a landlord evict a tenant without a court order?",
        "What is the economic loss doctrine in Utah contract law?",
        "What is the difference between Chapter 7 and Chapter 13 bankruptcy?",
    ]
    current_prompt_index: int = 0
    question_input: str = ""
    is_cycling_prompts: bool = False
    _vector_store: Chroma | None = None
    _retriever: BaseRetriever | None = None

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

    def _initialize_rag(self):
        """Initializes the RAG components (vector store and retriever)."""
        if self._retriever:
            return
        try:
            logging.info("Initializing RAG components...")
            api_key = os.environ.get("GOOGLE_API_KEY")
            if not api_key:
                logging.error("GOOGLE_API_KEY environment variable not set.")
                return
            embeddings = GoogleGenerativeAIEmbeddings(
                model="models/embedding-001", google_api_key=api_key
            )
            self._vector_store = Chroma(
                collection_name="ultima-collection",
                persist_directory="chromadata",
                embedding_function=embeddings,
            )
            self._retriever = self._vector_store.as_retriever(
                search_type="similarity", search_kwargs={"k": 2}
            )
            logging.info("RAG components initialized successfully.")
        except Exception as e:
            logging.exception(f"Error initializing RAG components: {e}")

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
        self._initialize_rag()
        if not self.is_cycling_prompts:
            self.is_cycling_prompts = True
            return ChatState.cycle_prompts

    @rx.event(background=True)
    async def process_question(self, form_data: dict):
        """Processes the user's question, runs RAG, and gets a response."""
        question = form_data.get("question", "").strip()
        if not question:
            return
        async with self:
            if self.is_typing:
                return
            self.is_typing = True
            self.messages.append({"text": question, "is_user": True})
            self.messages.append({"text": "", "is_user": False})
        try:
            self._initialize_rag()
            if not self._retriever:
                logging.error("Retriever not initialized.")
                async with self:
                    self.messages[-1]["text"] = (
                        "Error: The document retrieval system is not available."
                    )
                    self.is_typing = False
                return
            relevant_docs = await asyncio.to_thread(
                self._retriever.get_relevant_documents, question
            )
            context = """

""".join([doc.page_content for doc in relevant_docs])
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = f"You are a professional, helpful AI legal assistant designed to convey the context retrieved below to the user. Answer the user's question based on the following context. Whenever possible, respond to the user with the verbatim of the context, including the context’s citations to the law. For citations, use markdown to *italicize* case names. If the context does not contain the answer, state that you do not have enough information but can schedule a consultation. Do not mention that you are using 'context'.\n\nContext:\n{context}\n\nQuestion:\n{question}\n\nAnswer:"
            stream = await model.generate_content_async(prompt, stream=True)
            current_text = ""
            async for chunk in stream:
                if chunk.text:
                    current_text += chunk.text
                    async with self:
                        self.messages[-1]["text"] = current_text
        except Exception as e:
            logging.exception(f"An error occurred during question processing: {e}")
            error_message = f"An error occurred: {e}"
            if "quota" in str(e).lower():
                error_message = "I'm sorry, I am currently unable to answer questions due to high demand. Please try again later."
            async with self:
                self.messages[-1]["text"] = error_message
        finally:
            async with self:
                self.is_typing = False
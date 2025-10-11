import reflex as rx
from app.states.chat_state import ChatState, Message
from reflex.components.radix.themes.base import Theme

# Modern color palette
accent_color = "#4F46E5"  # A modern indigo
text_color = "#1F2937"  # Dark gray for better readability
border_color = "#E5E7EB"  # Lighter gray for subtle borders
user_bubble_bg = "rgba(229, 231, 235, 0.7)" # A slightly more opaque user bubble
ai_bubble_bg = "rgba(243, 244, 246, 0.7)" # A very light gray for the AI bubble

def message_bubble(message: Message) -> rx.Component:
    """A component to display a single chat message with a modern look."""
    
    # Common styles for the message text container
    bubble_style = {
        "padding": "0.75rem 1rem",
        "border_radius": "1rem",
        "max_width": "85%",
    }
    
    return rx.el.div(
        rx.el.div(
            rx.cond(
                message["is_user"],
                # Empty fragment for user messages
                rx.fragment(),
                # Larger, styled logo for AI messages
                rx.image(
                    src="/Law Practice Logo.png",
                    width="36px",
                    height="auto",
                    border_radius="50%",
                    box_shadow="0 2px 4px rgba(0,0,0,0.05)",
                ),
            ),
            rx.el.div(
                # Use a component map to disable TeX math rendering for dollar signs
                rx.markdown(
                    message["text"],
                    component_map={"span": lambda text: rx.el.span(text)},
                ),
                # Apply conditional background colors
                bg=rx.cond(
                    message["is_user"], user_bubble_bg, ai_bubble_bg
                ),
                # Apply shared bubble styles and specific border styles
                style=bubble_style,
                border=f"1px solid {border_color}",
                
            ),
            class_name="flex items-start gap-4",
        ),
        # Align the entire message bubble to the right for the user, left for the AI
        class_name=rx.cond(message["is_user"], "self-end justify-end", "self-start"),
        width="100%",
        display="flex",
    )


def chat_interface() -> rx.Component:
    """The main chat interface component with a sleek and modern design."""
    return rx.el.div(
        rx.el.h3(
            "Utah Caselaw Access Project",
            class_name="font-['DM Sans'] text-xl font-bold text-center mb-1 pt-6",
            color=text_color,
        ),
        rx.el.p(
            ChatState.messages[0]["text"],
            class_name="text-xs text-center text-gray-500 mb-4 px-6",
        ),
        rx.el.div(
            rx.foreach(ChatState.messages[1:], message_bubble),
            class_name="flex flex-col gap-4 p-4 h-[32rem] overflow-y-auto",
            id="chat-history" # Added an ID for potential future use (e.g., auto-scrolling)
        ),
        rx.cond(
            ChatState.is_typing,
            rx.el.div(
                rx.icon("loader", size=16, class_name=f"animate-spin text-[{accent_color}]"),
                rx.el.p("Minerva is thinking...", class_name="text-xs text-gray-500"),
                class_name="flex items-center gap-2 p-4",
            ),
            rx.fragment(),
        ),
        rx.el.form(
            rx.el.input(
                id="question_input",
                name="question",
                placeholder=ChatState.current_prompt_display,
                on_key_down=ChatState.handle_key_down,
                class_name=f"w-full bg-transparent focus:outline-none font-medium text-sm text-[{text_color}] placeholder:text-gray-400 placeholder:italic",
                default_value=ChatState.question_input,
                key=ChatState.question_input,
            ),
            rx.el.button(
                rx.icon("send", size=20, class_name=f"text-[{accent_color}]"),
                type="submit",
                class_name="p-3 rounded-full hover:bg-gray-100 transition-colors",
            ),
            on_submit=ChatState.process_question,
            reset_on_submit=True,
            class_name="flex items-center p-2 border-t",
            border_color=border_color,
        ),
        class_name=f"border rounded-xl w-full max-w-2xl mx-auto bg-white/80 backdrop-blur-md shadow-lg",
        border_color=border_color,
    )
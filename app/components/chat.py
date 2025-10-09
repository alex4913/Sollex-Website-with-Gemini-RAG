import reflex as rx
from app.states.chat_state import ChatState, Message

accent_color = "#F0C44D"
text_color = "#1A1A1A"
border_color = "#E0E0E0"


def message_bubble(message: Message) -> rx.Component:
    """A component to display a single chat message."""
    return rx.el.div(
        rx.el.div(
            rx.cond(
                message["is_user"],
                rx.fragment(),
                rx.icon("sun", size=24, class_name=f"text-[{accent_color}]"),
            ),
            rx.el.div(
                rx.el.p(message["text"], class_name="text-sm font-medium"),
                class_name="p-3 rounded-lg",
                bg=rx.cond(
                    message["is_user"], "rgba(224, 224, 224, 0.3)", "transparent"
                ),
            ),
            class_name="flex items-start gap-3",
        ),
        class_name=rx.cond(message["is_user"], "self-end", "self-start"),
        width="100%",
    )


def chat_interface() -> rx.Component:
    """The main chat interface component."""
    return rx.el.div(
        rx.el.h3(
            "Utah Caselaw Access Project",
            class_name="font-['DM Sans'] text-xl font-bold text-center mb-2 pt-6",
        ),
        rx.el.p(
            ChatState.messages[0]["text"],
            class_name="text-xs italic text-center text-red-600 mb-4 px-4",
        ),
        rx.el.div(
            rx.foreach(ChatState.messages[1:], message_bubble),
            class_name="flex flex-col gap-4 p-4 h-[32rem] overflow-y-auto",
        ),
        rx.cond(
            ChatState.is_typing,
            rx.el.div(
                rx.icon("loader", size=16, class_name="animate-spin"),
                rx.el.p("Minerva is thinking...", class_name="text-xs text-gray-500"),
                class_name="flex items-center gap-2 p-2",
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
                rx.icon("send", size=18, class_name=f"text-[{accent_color}]"),
                type="submit",
                class_name="p-2",
            ),
            on_submit=ChatState.process_question,
            reset_on_submit=True,
            class_name="flex items-center p-2 border-t",
            border_color=border_color,
        ),
        class_name=f"border rounded-none w-full max-w-2xl mx-auto bg-white/50 backdrop-blur-sm",
        border_color=border_color,
    )
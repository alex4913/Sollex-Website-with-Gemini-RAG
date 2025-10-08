import reflex as rx
from app.components.layout import layout
from app.states.contact_state import ContactState
from app.states.calendly_state import CalendlyState

border_color = "#E0E0E0"


def input_field(name: str, placeholder: str, type: str = "text") -> rx.Component:
    """A reusable input field component."""
    return rx.el.input(
        name=name,
        placeholder=placeholder,
        type=type,
        class_name="w-full bg-white/50 p-1.5 border focus:outline-none focus:ring-2 focus:ring-[#F0C44D]",
        border_color=border_color,
        required=True,
    )


def contact_form() -> rx.Component:
    """The contact form component."""
    return rx.el.form(
        rx.el.div(
            input_field("name", "Name"),
            input_field("email", "Email", type="email"),
            input_field("phone", "Phone Number", type="tel"),
            rx.el.textarea(
                name="message",
                placeholder="Your Message",
                class_name="w-full bg-white/50 p-1.5 border focus:outline-none focus:ring-2 focus:ring-[#F0C44D] min-h-24",
                border_color=border_color,
                required=True,
            ),
            rx.el.button(
                "Send Message",
                type="submit",
                class_name="w-full bg-[#F0C44D] text-[#1A1A1A] font-bold py-2 hover:opacity-90 transition-opacity",
            ),
            class_name="flex flex-col gap-2",
        ),
        on_submit=ContactState.handle_submit,
        reset_on_submit=True,
    )


def calendly_widget() -> rx.Component:
    """The Calendly widget component."""
    return rx.el.div(
        id="calendly-widget",
        on_mount=CalendlyState.init_calendly,
        class_name="min-w-[320px] h-[600px] w-full",
    )


def contact() -> rx.Component:
    """The main contact page."""
    return layout(
        rx.el.div(
            rx.el.h1(
                "Schedule a Consultation",
                class_name="font-['DM Sans'] text-4xl font-bold mb-2",
            ),
            rx.el.p(
                "Book a 30-minute consultation directly or send a message below.",
                class_name="text-lg text-gray-600 mb-4",
            ),
            calendly_widget(),
            rx.el.div(
                rx.el.h2(
                    "Send a Message",
                    class_name="font-['DM Sans'] text-3xl font-bold mt-8 mb-4",
                ),
                rx.el.div(
                    contact_form(),
                    rx.el.div(
                        rx.el.h3(
                            "Firm Details",
                            class_name="font-['DM Sans'] text-xl font-bold mb-2",
                        ),
                        rx.el.p(
                            "Law Office of Alexander S. Chang",
                            class_name="font-semibold",
                        ),
                        rx.el.p(
                            "Address available upon consultation.",
                            class_name="font-medium",
                        ),
                        rx.el.p("Salt Lake City, UT", class_name="font-medium"),
                        rx.el.p("Phone: (123) 456-7890", class_name="font-medium mt-2"),
                        class_name="space-y-0 text-left",
                    ),
                    class_name="grid md:grid-cols-2 gap-8 w-full max-w-4xl",
                ),
            ),
            class_name="flex flex-col items-center text-center",
        )
    )
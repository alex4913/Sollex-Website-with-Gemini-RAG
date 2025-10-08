import reflex as rx
from app.components.layout import layout


def disclaimer() -> rx.Component:
    """Legal disclaimer page."""
    return layout(
        rx.el.div(
            rx.el.h1(
                "Disclaimer", class_name="font-['DM Sans'] text-4xl font-bold mb-6"
            ),
            rx.el.div(
                rx.el.p(
                    "The information provided on this website is for general informational purposes only and does not, and is not intended to, constitute legal advice. No attorney-client relationship is formed by the use of this website, including its AI chat feature.",
                    class_name="mb-4",
                ),
                rx.el.p(
                    "This website should not be used as a substitute for competent legal advice from a licensed professional attorney in your jurisdiction. You should not act or refrain from acting based on any content on this site without seeking legal or other professional advice.",
                    class_name="mb-4",
                ),
                rx.el.p(
                    "The content of any communication sent to the Law Office of Alexander S. Chang or any of its personnel at the email addresses set forth in this website will not create an attorney-client relationship and will not be treated as confidential. Please do not send any confidential information until such a time as an attorney-client relationship has been established.",
                    class_name="mb-4",
                ),
                rx.el.p(
                    "The AI assistant is a tool for preliminary information and is not a lawyer. It may produce inaccurate information. Any information provided by the AI does not constitute legal advice and does not create an attorney-client privilege.",
                    class_name="font-semibold",
                ),
                class_name="space-y-4 text-gray-700 leading-relaxed",
            ),
            class_name="max-w-3xl mx-auto",
        )
    )
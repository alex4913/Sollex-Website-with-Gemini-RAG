import reflex as rx
from app.components.layout import layout

accent_color = "#F0C44D"
text_color = "#1A1A1A"


def feature_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, size=32, class_name=f"text-[{accent_color}] mb-4"),
        rx.el.h3(title, class_name="font-['DM Sans'] text-xl font-bold mb-2"),
        rx.el.p(description, class_name="text-gray-600 text-sm leading-relaxed"),
        class_name="flex flex-col items-center text-center p-6",
    )


def index() -> rx.Component:
    """The home page of the website."""
    return layout(
        rx.el.div(
            rx.el.h1(
                "Sharp Counsel. Clear Results.",
                class_name="font-['DM Sans'] text-5xl md:text-6xl font-bold text-center mb-6 leading-tight",
            ),
            rx.el.p(
                "The Law Office of Alexander S. Chang provides sophisticated legal expertise, delivering quality, affordable, and precise legal services through a modern, client-focused approach.",
                class_name="max-w-3xl mx-auto text-center text-gray-700 text-lg mb-12",
            ),
            rx.el.a(
                rx.el.button(
                    "Access Utah's Open-Source Legal Database",
                    rx.icon("arrow-right", class_name="ml-2"),
                    class_name=f"bg-[{accent_color}] text-[{text_color}] font-bold py-3 px-8 hover:opacity-90 transition-opacity inline-flex items-center",
                ),
                href="/minerva",
            ),
            rx.el.div(
                rx.el.h2(
                    "A Modern Firm Built on Timeless Values",
                    class_name="font-['DM Sans'] text-3xl font-bold text-center mt-6 mb-12",
                ),
                rx.el.div(
                    feature_card(
                        "lightbulb",
                        "Innovative Efficiency",
                        "We use advanced legal technology to streamline research and document preparation, delivering data-driven strategies that save you valuable time and resources.",
                    ),
                    feature_card(
                        "scale",
                        "Access to Justice",
                        "Our Modest Means Program offers tiered, flat-fee pricing to make high-quality legal services accessible to lower and middle-income individuals.",
                    ),
                    feature_card(
                        "shield-check",
                        "Client-Centered Focus",
                        "We demystify the legal process. You receive clear guidance and direct attention, empowering you to make informed decisions for your future.",
                    ),
                    class_name="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto",
                ),
                class_name="w-full mt-16",
            ),
            class_name="flex flex-col items-center",
        )
    )
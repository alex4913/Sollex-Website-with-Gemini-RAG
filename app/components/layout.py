import reflex as rx
from app.states.base_state import BaseState

accent_color = "#F0C44D"
text_color = "#1A1A1A"
nav_links = [
    ("Attorney Profile", "/profile"),
    ("Modest Means Program", "/modest-means"),
    ("Contact", "/contact"),
]


def nav_link(text: str, url: str) -> rx.Component:
    """A navigation link that highlights the active page."""
    return rx.el.a(
        rx.el.p(
            text,
            class_name=rx.cond(
                BaseState.current_page == url,
                f"text-[{accent_color}] font-semibold",
                f"text-[{text_color}] hover:text-[{accent_color}] transition-colors font-medium",
            ),
        ),
        href=url,
    )


def navbar() -> rx.Component:
    """The navigation bar for the website."""
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.image(
                    src="/Law Practice Logo.png",
                    alt="Sollex Legal Logo",
                    class_name="h-10 w-auto",
                ),
                href="/",
            ),
            rx.el.nav(
                rx.foreach(nav_links, lambda link: nav_link(link[0], link[1])),
                class_name="hidden md:flex items-center gap-8",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("menu", size=24),
                    on_click=BaseState.toggle_mobile_menu,
                    class_name=f"md:hidden text-[{text_color}]",
                ),
                class_name="md:hidden",
            ),
            class_name="flex justify-between items-center w-full max-w-6xl mx-auto py-5 px-4 md:px-6",
        ),
        rx.cond(
            BaseState.show_mobile_menu,
            rx.el.div(
                rx.el.nav(
                    rx.foreach(nav_links, lambda link: nav_link(link[0], link[1])),
                    class_name="flex flex-col items-center gap-4 py-4",
                ),
                class_name="md:hidden bg-[#FDFDFD]/95 backdrop-blur-sm",
            ),
        ),
        class_name="w-full bg-[#FDFDFD]/80 backdrop-blur-sm sticky top-0 z-50 border-b border-[#E0E0E0]/50",
    )


def footer() -> rx.Component:
    """The footer for the website."""
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    f"© 2025 Sollex Legal, L3C", class_name="text-sm text-gray-500"
                ),
                rx.el.div(
                    rx.el.a(
                        "Disclaimer",
                        href="/disclaimer",
                        class_name="text-sm text-gray-500 hover:text-black",
                    ),
                    rx.el.a(
                        "Privacy Policy",
                        href="/privacy-policy",
                        class_name="text-sm text-gray-500 hover:text-black",
                    ),
                    class_name="flex gap-4",
                ),
                class_name="flex justify-between items-center",
            ),
            class_name="max-w-6xl mx-auto py-8 px-4 md:px-6",
        ),
        class_name="border-t border-[#E0E0E0]",
    )


def layout(child: rx.Component) -> rx.Component:
    """The main layout for all pages."""
    return rx.el.main(
        rx.el.div(
            class_name="absolute top-0 left-0 w-96 h-96 bg-[#F0C44D]/10 rounded-full -translate-x-1/2 blur-3xl opacity-70 z-0"
        ),
        rx.el.div(
            class_name="absolute bottom-0 right-0 w-[32rem] h-[32rem] bg-[#F0C44D]/10 rounded-full translate-x-1/2 blur-3xl opacity-70 z-0"
        ),
        rx.el.div(
            navbar(),
            rx.el.div(
                child, class_name="w-full max-w-6xl mx-auto px-4 md:px-6 py-8 md:py-12"
            ),
            footer(),
            class_name="relative z-10",
        ),
        class_name="font-['Inter'] main-background relative overflow-x-hidden",
        color=text_color,
    )
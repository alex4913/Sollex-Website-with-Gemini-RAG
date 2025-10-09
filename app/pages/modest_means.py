import reflex as rx
from app.components.layout import layout

accent_color = "#F0C44D"
border_color = "#E0E0E0"


def tier_card(
    tier: str, income_range: str, details: list[str], icon: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name=f"text-[{accent_color}]", size=32),
            class_name="absolute -top-5 -left-5 bg-white p-3 rounded-full border",
            border_color=border_color,
        ),
        rx.el.h3(
            f"Level {tier}", class_name="font-['DM Sans'] text-2xl font-bold mb-3"
        ),
        rx.el.p(income_range, class_name="font-semibold text-base mb-4 text-gray-800"),
        rx.el.ul(
            rx.foreach(
                details,
                lambda item: rx.el.li(
                    rx.icon("check", class_name=f"text-green-500 mr-2 h-4 w-4"),
                    item,
                    class_name="flex items-start text-sm text-gray-600",
                ),
            ),
            class_name="space-y-2 list-none",
        ),
        class_name="bg-white p-8 border rounded-lg shadow-sm relative",
        border_color=border_color,
    )


def modest_means() -> rx.Component:
    return layout(
        rx.el.div(
            rx.el.h1(
                "Modest Means Program",
                class_name="font-['DM Sans'] text-4xl md:text-5xl font-bold text-center mb-4",
            ),
            rx.el.p(
                "Leveraging the latest technology to provide affordable, high-quality legal services for our community.",
                class_name="text-lg text-gray-600 text-center mb-16 max-w-3xl mx-auto",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Commitment to Access to Justice",
                        class_name="font-['DM Sans'] text-3xl font-bold mb-4",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "The Law Office of Alexander S. Chang is committed to bridging the access to justice gap. The vast majority of individuals and families earn too much to qualify for free legal aid from non-profits, but not enough to afford traditional legal fees. The Law Office of Alexander S. Chang is a proud participant of the ",
                            rx.el.a(
                                "Utah State Bar’s Modest Means Program",
                                href="https://www.utahbar.org/accesstojustice/modest-means/",
                                class_name=f"text-[{accent_color}] hover:underline font-semibold",
                                target="_blank",
                                rel="noopener noreferrer",
                            ),
                            ", which is designed specifically to serve this group.",
                            class_name="mb-4 text-justify",
                        ),
                        rx.el.p(
                            "By using the latest technology and streamlined processes, we can offer high-quality legal services at significantly reduced rates. Our goal is to ensure that everyone, regardless of income, has access to capable legal representation.",
                            class_name="text-justify",
                        ),
                    ),
                ),
                rx.el.div(
                    rx.icon("gavel", size=80, class_name=f"text-[{accent_color}]/50")
                ),
                class_name="grid md:grid-cols-2 gap-12 items-center bg-white/50 p-8 rounded-lg border",
                border_color=border_color,
            ),
            rx.el.div(
                rx.el.h2(
                    "Tiered Fee Structure",
                    class_name="font-['DM Sans'] text-3xl font-bold text-center mt-16 mb-10",
                ),
                rx.el.div(
                    tier_card(
                        "1",
                        "Income: 125% - 200% FPG",
                        [
                            "Lowest flat-fee services.",
                            "Significantly reduced hourly rate.",
                            "Ideal for those with the most need.",
                        ],
                        "star",
                    ),
                    tier_card(
                        "2",
                        "Income: 200% - 300% FPG",
                        [
                            "Reduced flat-fee packages.",
                            "Reduced hourly rate.",
                            "For lower-to-middle income individuals.",
                        ],
                        "coins",
                    ),
                    tier_card(
                        "3",
                        "Income: 300% - 400% FPG",
                        [
                            "Competitive flat-fee packages.",
                            "Moderately reduced hourly rate.",
                            "For predictable middle-income costs.",
                        ],
                        "landmark",
                    ),
                    class_name="grid md:grid-cols-3 gap-8",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "Based on Federal Poverty Guidelines (FPG) for a family of 3 (current estimates):",
                            class_name="font-semibold text-gray-700 text-center text-sm",
                        ),
                        rx.el.div(
                            rx.el.p("125% ≈ $34,645/year"),
                            rx.el.p("200% ≈ $53,300/year"),
                            rx.el.p("300% ≈ $79,950/year"),
                            rx.el.p("400% ≈ $106,600/year"),
                            class_name="grid grid-cols-2 md:grid-cols-4 gap-x-4 gap-y-1 text-center text-xs text-gray-600",
                        ),
                        class_name="space-y-2",
                    ),
                    class_name="max-w-2xl mx-auto mt-6 text-center bg-white/50 p-4 border rounded-lg",
                    border_color=border_color,
                ),
                rx.el.p(
                    "Clients with income above 400% FPG do not qualify for the Modest Means Program but may be accepted at standard firm rates.",
                    class_name="text-center text-sm text-gray-600 mt-4",
                ),
            ),
            rx.el.div(
                rx.el.h2(
                    "How to Qualify",
                    class_name="font-['DM Sans'] text-3xl font-bold text-center mt-16 mb-8",
                ),
                rx.el.ol(
                    rx.el.li(
                        "Schedule an initial consultation through our contact page."
                    ),
                    rx.el.li(
                        "Provide income verification documents (e.g., recent pay stubs, tax returns)."
                    ),
                    rx.el.li(
                        "We will confirm your eligibility tier and provide a clear fee agreement before any work begins."
                    ),
                    class_name="list-decimal list-inside space-y-2 max-w-2xl mx-auto text-gray-700 bg-white/50 p-6 border rounded-lg",
                    border_color=border_color,
                ),
            ),
            class_name="w-full",
        )
    )
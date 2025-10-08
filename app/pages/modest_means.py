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
        rx.el.h3(f"Tier {tier}", class_name="font-['DM Sans'] text-2xl font-bold mb-3"),
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
                    rx.el.p(
                        "The Law Office of Alexander S. Chang is committed to bridging the access to justice gap. The vast majority of individuals and families earn too much to qualify for free legal aid from non-profits, but not enough to afford traditional legal fees. The Law Office of Alexander S. Chang is a proud participant of the [Utah State Bar’s Modest Means Program](https://www.utahbar.org/accesstojustice/modest-means/), which is designed specifically to serve this group.",
                        class_name="mb-4",
                    ),
                    rx.el.p(
                        "By leveraging the power of AI-driven tools and streamlined processes, we can offer high-quality legal services at significantly reduced rates. Our goal is to ensure that everyone, regardless of income, has access to capable legal representation.",
                        class_name="",
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
                    class_name="font-['DM Sans'] text-3xl font-bold text-center mt-20 mb-12",
                ),
                rx.el.div(
                    tier_card(
                        "1",
                        "Income: 125% - 300% FPG",
                        [
                            "Lowest flat-fee services.",
                            "Significantly reduced hourly rate.",
                            "Ideal for those with the most need.",
                        ],
                        "gem",
                    ),
                    tier_card(
                        "2",
                        "Income: 300% - 500% FPG",
                        [
                            "Competitive flat-fee packages.",
                            "Moderately reduced hourly rate.",
                            "For predictable middle-income costs.",
                        ],
                        "coins",
                    ),
                    tier_card(
                        "3",
                        "Income: > 500% FPG",
                        [
                            "Standard competitive rates.",
                            "Supports our community mission.",
                            "Fees help subsidize Tiers 1 & 2.",
                        ],
                        "landmark",
                    ),
                    class_name="grid md:grid-cols-3 gap-12 mt-8",
                ),
                rx.el.p(
                    "FPG: Federal Poverty Guidelines.",
                    class_name="text-center text-sm text-gray-500 mt-4",
                ),
            ),
            rx.el.div(
                rx.el.h2(
                    "How to Qualify",
                    class_name="font-['DM Sans'] text-3xl font-bold text-center mt-20 mb-8",
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
import reflex as rx
from app.components.layout import layout

accent_color = "#F0C44D"
border_color = "#E0E0E0"


def blockquote(text: str) -> rx.Component:
    """A styled blockquote component."""
    return rx.el.blockquote(
        rx.el.p(
            f'"{text}"',
            class_name="text-lg italic font-medium leading-relaxed text-gray-800",
        ),
        class_name=f"border-l-4 pl-6 my-8",
        border_color=f"[{accent_color}]",
    )


def expertise_item(icon: str, title: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, class_name=f"text-[{accent_color}]", size=24),
        rx.el.p(title, class_name="font-semibold text-gray-800"),
        class_name="flex items-center gap-3 p-3 bg-white/50 rounded-lg border",
        border_color=border_color,
    )


def publication(title: str, citation: str, url: str | None = None) -> rx.Component:
    title_component = rx.el.p(title, class_name="font-semibold text-gray-800")
    if url:
        title_component = rx.el.a(
            title_component,
            href=url,
            target="_blank",
            rel="noopener noreferrer",
            class_name="hover:underline",
        )
    return rx.el.div(
        title_component,
        rx.el.p(citation, class_name="text-sm text-gray-600"),
        class_name="py-4 border-b",
        border_color=border_color,
    )


def professional_item(title: str, description: str) -> rx.Component:
    return rx.el.div(
        rx.el.p(title, class_name="font-semibold text-gray-800"),
        rx.el.p(description, class_name="text-sm text-gray-600"),
        class_name="py-4",
    )


def speaking_engagement(event: str, role: str, date: str) -> rx.Component:
    return rx.el.div(
        rx.icon("mic", class_name=f"text-[{accent_color}] w-5 h-5 mr-4 mt-1", size=18),
        rx.el.div(
            rx.el.p(f"{role} on “{event}”", class_name="font-semibold text-gray-800"),
            rx.el.p(date, class_name="text-sm text-gray-600"),
        ),
        class_name="flex items-start py-3 border-b",
        border_color=border_color,
    )


def profile() -> rx.Component:
    return layout(
        rx.el.div(
            rx.el.div(
                rx.image(
                    src="/SJQ Photo (Nov 2021).jpg",
                    alt="Alexander S. Chang Headshot",
                    class_name="w-full h-full object-cover",
                ),
                class_name="w-40 h-40 md:w-56 md:h-56 rounded-full overflow-hidden flex-shrink-0 shadow-lg mx-auto border-4 border-white",
            ),
            rx.el.div(
                rx.el.h1(
                    "Alexander S. Chang",
                    class_name="font-['DM Sans'] text-4xl md:text-5xl font-bold mt-6 text-center",
                ),
                rx.el.h2(
                    "Principal Attorney",
                    class_name=f"text-xl font-medium text-center text-transparent bg-clip-text bg-gradient-to-r from-[{accent_color}] to-[#E6B83A] mb-8",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Young Lawyer of the Year (2024)",
                            class_name="font-['DM Sans'] text-2xl font-bold",
                        ),
                        rx.el.p(
                            "Awarded by the Utah State Bar",
                            class_name="text-md text-gray-600",
                        ),
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Award photo placeholder",
                            class_name="text-sm text-gray-500",
                        ),
                        class_name="bg-gray-100 border border-dashed rounded-lg h-48 mt-4 flex items-center justify-center",
                    ),
                    class_name="max-w-md mx-auto bg-white/60 p-6 rounded-lg border text-center",
                    border_color=border_color,
                ),
                blockquote(
                    "My mission is to demystify the legal process, to empower clients to make informed decisions about their future."
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "About",
                            class_name="font-['DM Sans'] text-2xl font-bold mb-4",
                        ),
                        rx.el.p(
                            "Alexander S. Chang is recognized within the Utah legal community as an expert in the intersection of law and legal technology. He was named the Utah State Bar's Young Lawyer of the Year for 2024. He founded the Law Office of Alexander S. Chang with a dual mission: to provide sharp, forward-thinking legal counsel and to leverage modern technology to make legal services more accessible and affordable.",
                            class_name="text-gray-700 leading-relaxed text-justify",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "Areas of Expertise",
                            class_name="font-['DM Sans'] text-2xl font-bold mb-4",
                        ),
                        rx.el.div(
                            expertise_item("cpu", "AI in Legal Practice"),
                            expertise_item("briefcase", "General Litigation"),
                            expertise_item("archive", "Small Business Law"),
                            expertise_item("shield", "Trust Law"),
                            expertise_item("file", "Contract Law"),
                            expertise_item("scale", "Access to Justice"),
                            class_name="grid sm:grid-cols-2 gap-4",
                        ),
                    ),
                    class_name="grid md:grid-cols-2 gap-12 my-12",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Commitee Appointments",
                            class_name="font-['DM Sans'] text-2xl font-bold mb-4 text-center",
                        ),
                        professional_item(
                            "Utah State Bar Standing Committee on AI",
                            "Member, Appointment from Sep 2025 onwards",
                        ),
                        professional_item(
                            "Utah Supreme Court Ad Hoc Committee on Regulatory Reform, AI and Legal Technology",
                            "Work Group Member, Apr 2025 - Dec 2026",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "Scholarship",
                            class_name="font-['DM Sans'] text-2xl font-bold mb-4 text-center",
                        ),
                        publication(
                            "A Lawyer’s Guide to Artificial Intelligence and its Use in the Practice of Law",
                            "Co-author, Utah Bar Journal, Vol. 37 No. 2 | Mar/Apr 2024",
                            url="https://www.utahbar.org/wp-content/uploads/2024/03/2024_FINAL_02_Mar_Apr-1.pdf#page=16",
                        ),
                        publication(
                            "Resolving The Dahl Conundrum: The Public Policy Conflict Between Asset Protection Trusts and The Equitable Division of Marital Assets",
                            "Co-author, Utah Bar Journal, Vol. 35 No. 6 | Nov/Dec 2022",
                            url="https://www.utahbar.org/wp-content/uploads/2023/04/2022_FINAL_06_Nov_Dec.pdf#page=44",
                        ),
                    ),
                    class_name="grid md:grid-cols-2 gap-12 my-12 max-w-5xl mx-auto w-full",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Speaking Engagements",
                        class_name="font-['DM Sans'] text-2xl font-bold mb-4 text-center",
                    ),
                    speaking_engagement(
                        "2025 Access to Justice Summit Technology Panel",
                        "Panelist",
                        "Utah State Bar Center, October 3, 2025",
                    ),
                    speaking_engagement(
                        "Navigating Human Connection in the World of AI",
                        "Panelist",
                        "Zions Bancorporation Technology Center, August 14, 2025",
                    ),
                    speaking_engagement(
                        "Artificial Intelligence & Ethics",
                        "Presenter",
                        "Bankruptcy Section of the Utah Bar, November 19, 2024",
                    ),
                    speaking_engagement(
                        "Artificial Intelligence in the Practice of Law",
                        "Speaker and Discussion Leader",
                        "The American Bankruptcy Institute’s Rocky Mountain Bankruptcy Conference, June 12-14, 2024",
                    ),
                    speaking_engagement(
                        "Brown Bag Session on Artificial Intelligence Policy",
                        "Presenter",
                        "Utah Appellate Courts, May 9, 2024",
                    ),
                    speaking_engagement(
                        "Technology Opportunities, Duties, and Headaches",
                        "Presenter",
                        "Inns of Court Group CLE Series, April 17, 2024",
                    ),
                    class_name="max-w-3xl mx-auto w-full mt-12",
                ),
            ),
            class_name="flex flex-col items-center",
        )
    )
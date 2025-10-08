import reflex as rx
from app.components.layout import layout


def privacy_policy() -> rx.Component:
    """Privacy policy page."""
    return layout(
        rx.el.div(
            rx.el.h1(
                "Privacy Policy", class_name="font-['DM Sans'] text-4xl font-bold mb-6"
            ),
            rx.el.div(
                rx.el.p(
                    "The Law Office of Alexander S. Chang ('we', 'us', or 'our') is committed to protecting your privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our website, including any other media form, media channel, mobile website, or mobile application related or connected thereto (collectively, the 'Site').",
                    class_name="mb-4",
                ),
                rx.el.h2(
                    "Collection of Your Information",
                    class_name="font-['DM Sans'] text-2xl font-bold my-4",
                ),
                rx.el.p(
                    "We may collect information about you in a variety of ways. The information we may collect on the Site includes personally identifiable information, such as your name, shipping address, email address, and telephone number, and demographic information, such as your age, gender, hometown, and interests, that you voluntarily give to us when you register with the Site or when you choose to participate in various interactive features of the Site, such as online chat and message boards.",
                    class_name="mb-4",
                ),
                rx.el.h2(
                    "Use of Your Information",
                    class_name="font-['DM Sans'] text-2xl font-bold my-4",
                ),
                rx.el.p(
                    "Having accurate information about you permits us to provide you with a smooth, efficient, and customized experience. Specifically, we may use information collected about you via the Site to create and manage your account, email you regarding your account or order, and respond to your inquiries.",
                    class_name="mb-4",
                ),
                rx.el.h2(
                    "Chatbot Data",
                    class_name="font-['DM Sans'] text-2xl font-bold my-4",
                ),
                rx.el.p(
                    "Conversations with our AI assistant may be logged and reviewed for quality assurance and to improve our services. Do not share sensitive personal information in the chat that you would not want recorded.",
                    class_name="mb-4 font-semibold",
                ),
                rx.el.h2(
                    "Contact Us", class_name="font-['DM Sans'] text-2xl font-bold my-4"
                ),
                rx.el.p(
                    "If you have questions or comments about this Privacy Policy, please contact us through the form on our contact page.",
                    class_name="mb-4",
                ),
                class_name="space-y-4 text-gray-700 leading-relaxed",
            ),
            class_name="max-w-3xl mx-auto",
        )
    )
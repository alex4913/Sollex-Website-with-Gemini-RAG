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
                    "Sollex Legal, L3C d/b/a “The Law Office of Alexander S. Chang” (“Sollex,” “we,” “our,” or “us”) is committed to protecting your privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our website, including any other media form, media channel, mobile website, or mobile application related or connected thereto (collectively, the “Site”). Please read this Privacy Policy carefully to understand our practices regarding your information and our commitment to protecting it.",
                    class_name="mb-4",
                ),
                rx.el.h2(
                    "Collection of Your Information",
                    class_name="font-['DM Sans'] text-2xl font-bold my-4",
                ),
                rx.el.p(
                    "We may collect basic information about you in a variety of ways. The information we may collect on the Site includes basic contact information, such as your name, address, e-mail address, and telephone number that you voluntarily give to us when you submit an inquiry through the Site or when you choose to participate in various interactive features of the Site, such as the website message system and the Utah Caselaw Access Project (“UCAP”). DO NOT SEND CONFIDENTIAL INFORMATION THROUGH THE SITE.",
                    class_name="mb-4",
                ),
                rx.el.h2(
                    "Use of Your Information",
                    class_name="font-['DM Sans'] text-2xl font-bold my-4",
                ),
                rx.el.p(
                    "We may use the information we collect for the following purposes, grounded in our commitment to serving legal professionals responsibly: (1) to respond to your inquiries, troubleshoot technical issues, and provide assistance with using the Site; (2) to understand how users interact with our Site, allowing us to improve the functionality, usability, and performance of our Site for all users; (3) to detect, investigate, and prevent fraudulent transactions, unauthorized access, and other illegal activities, and to protect our rights, property, and the security of our Site and users; and (4) to comply with our legal obligations, resolve disputes, and enforce our agreements (including this Privacy Policy).",
                    class_name="mb-4",
                ),
                rx.el.h2(
                    "UCAP Data", class_name="font-['DM Sans'] text-2xl font-bold my-4"
                ),
                rx.el.p(
                    "Inquires and access to our AI-powered Utah Caselaw Access Project is logged and reviewed for quality assurance. UCAP is specifically designed to reject any requests for legal advice, or the application of law to your specific set of facts. DO NOT SHARE SENSITIVE PERSONAL OR CONFIDENTIAL INFORMATION YOUR INQUIRES TO UCAP.",
                    class_name="mb-4",
                ),
                rx.el.h2(
                    "Contact Us", class_name="font-['DM Sans'] text-2xl font-bold my-4"
                ),
                rx.el.p(
                    "If you have questions or comments about this Privacy Policy, please contact us through the form on our contact page or directly by e-mail at alexander@utahlaw.ai.",
                    class_name="mb-4",
                ),
                class_name="space-y-4 text-gray-700 leading-relaxed",
            ),
            class_name="max-w-3xl mx-auto",
        )
    )
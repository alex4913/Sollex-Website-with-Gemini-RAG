import reflex as rx
from app.components.layout import layout
from app.pages.index import index
from app.pages.profile import profile
from app.pages.contact import contact
from app.pages.modest_means import modest_means
from app.pages.disclaimer import disclaimer
from app.pages.privacy_policy import privacy_policy
from app.pages.minerva import minerva
from app.states.chat_state import ChatState

app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=["/styles.css"],
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Inter:wght@400;500;600&display=swap",
            rel="stylesheet",
        ),
        rx.el.script(
            src="https://assets.calendly.com/assets/external/widget.js", async_=True
        ),
    ],
)
app.add_page(index)
app.add_page(minerva, route="/minerva")
app.add_page(profile, route="/profile")
app.add_page(contact, route="/contact")
app.add_page(modest_means, route="/modest-means")
app.add_page(disclaimer, route="/disclaimer")
app.add_page(privacy_policy, route="/privacy-policy")
import reflex as rx
import logging


class ContactState(rx.State):
    """Manages the state for the contact form."""

    form_data: dict[str, str] = {}
    form_submitted: bool = False

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submission."""
        self.form_data = form_data
        logging.info(f"Contact form submitted: {self.form_data}")
        self.form_submitted = True
        yield rx.toast("Thank you for your message! We will be in touch shortly.")
        yield ContactState.reset_form

    @rx.event
    def reset_form(self):
        self.form_data = {}
        self.form_submitted = False
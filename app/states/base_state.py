import reflex as rx


class BaseState(rx.State):
    """State to manage global properties like current page."""

    show_mobile_menu: bool = False

    @rx.var
    def current_page(self) -> str:
        """Returns the current page path."""
        return self.router.page.path

    @rx.event
    def toggle_mobile_menu(self):
        """Toggles the visibility of the mobile menu."""
        self.show_mobile_menu = not self.show_mobile_menu
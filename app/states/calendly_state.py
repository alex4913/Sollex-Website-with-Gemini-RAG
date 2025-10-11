import reflex as rx


class CalendlyState(rx.State):
    """State to manage the Calendly widget."""

    @rx.event
    def init_calendly(self):
        """Initializes the Calendly inline widget."""
        return rx.call_script("""
            if (window.Calendly) {
                const el = document.getElementById('calendly-widget');
                // Clear the element before initializing to prevent duplicates
                if (el) {
                    el.innerHTML = '';
                    Calendly.initInlineWidget({
                        url: 'https://calendly.com/alex-law-office/30-minute-consultation',
                        parentElement: el,
                    });
                }
            }
            """)
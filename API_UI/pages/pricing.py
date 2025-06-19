import reflex as rx
from ..ui.base import base_page
from .. import navigation

def pricing_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Pricing", size="9", text_align="center"),
            rx.text(
                "Some text about pricing."
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my_child"
        )
    return base_page(my_child, hide_navbar=False)
import reflex as rx
import reflex_local_auth
from ..ui.base import base_page
from . import form

@reflex_local_auth.require_login
def get_data_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Entities GET DATA Form", size="9", text_align="center"),
            rx.desktop_only(
                rx.box(
                    form.form_get_component(),
                    padding="20px",
                    max_width="600px"
                )
            ),
            rx.tablet_only(
                rx.box(
                    form.form_get_component(),
                    padding="20px",
                    width="50vw"
                )
            ),
            rx.mobile_only(
                rx.box(
                    form.form_get_component(),
                    padding="20px",
                    width="30vw"
                )
            ),
            spacing="5",
            justify="start",
            align="center",
            min_height="80vh",
            id="my_child"
        )
    return base_page(my_child)
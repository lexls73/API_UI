import reflex as rx
from ..ui.base import base_page
from . import forms

def blog_post_add_page() -> rx.Component:
    my_form = forms.blog_post_add_form()
    my_child = rx.vstack(
            rx.heading("New Blog Post", size="9", text_align="center"),
            rx.desktop_only(
                rx.box(
                    my_form,
                    width="50vw"
                )
            ),
            rx.tablet_only(
                rx.box(
                    my_form,
                    width="75vw"
                )
            ),
            rx.mobile_only(
                rx.box(
                    my_form,
                    width="85vw"
                )
            ),
            spacing="5",
            align="center",
            min_height="90vh"
        )
    return base_page(my_child, hide_navbar=False)
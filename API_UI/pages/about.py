import reflex as rx
from ..ui.base import base_page
from .. import navigation

def about_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("About us", size="9", text_align="center"),
            rx.text(
                "This application was created by Alejandro Lopez Stanley using Reflex. It uses the Aizon API client to connect to the platform."
            ),
            rx.text("It uses Python 3.11, reflex & bigfinitAPIClient"),
            rx.text("In Entities ABM you can manage entities using an Excel template."),
            rx.text("The connection is made with the configuration file located in the path:"),
            rx.text("/Users/<<user>>/.config/BigfiniteAPIClient"),
            spacing="5",
            justify="center",
            align="center",
            min_height="89vh",
            id="my_child"
        )
    return base_page(my_child, hide_navbar=False)
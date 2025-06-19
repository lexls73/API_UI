"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import reflex_local_auth

from rxconfig import config
from .ui.base import base_page
from .auth.pages import(
    my_login_page,
    my_registration_page,
    my_logout_page
)
from .auth.state import SessionState
from . import navigation,pages,entities,cfg

class State(rx.State):
    label = "Hello, Reflex!"
    
    def handle_title_input_change(self, value: str):
        """Update the label when the input changes."""
        self.label = value
    
    def did_click(self):
        return rx.redirect(navigation.routes.ABOUT_ROUTE)

def index() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Welcome to Aizon API Utility!", size="9", text_align="center"),
            rx.text(
                "This is a simple app to use API and is doing using Reflex.",
                size="5",
                text_align="center",
            ),
            #rx.button("About Us",on_click=State.did_click, size="4"),
            spacing="5",
            justify="center",
            align="center",
            text_align="center",
            min_height="89vh",
            id="my_child"
        )

    return base_page(my_child, hide_navbar=False)

app = rx.App(
        theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="indigo",
    )
)

# Index
app.add_page(index)
###############################
# Reflex local auth pages
app.add_page(
    my_login_page,
    route=reflex_local_auth.routes.LOGIN_ROUTE,
    title="Login",
)
app.add_page(
    my_registration_page,
    route=reflex_local_auth.routes.REGISTER_ROUTE,
    title="Register",
)
###############################
# My Pages
app.add_page(
    pages.about_page,
    route=navigation.routes.ABOUT_ROUTE, 
    title="About Us"
    )
app.add_page(
    entities.abm_page ,
    route=navigation.routes.ENTITIES_ABM, 
    title="Enities CRUD",
    on_load=entities.EntitiesState.reset_fields
    )
app.add_page(
        cfg.cfg_page,
        route=navigation.routes.CONFIGURATION_PAGE, 
        title="Configuration",
        on_load=cfg.BigfiniteCfgState.reset_fields
    )
app.add_page(
        my_logout_page,
        route=navigation.routes.LOGOUT_ROUTE, 
        title="logout"
    )
###############################
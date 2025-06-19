import reflex as rx
from reflex_local_auth.pages.login import LoginState, login_form, PADDING_TOP
from reflex_local_auth.pages.registration import RegistrationState, register_form
from ..ui.base import base_page
from .. import navigation
from .forms import my_register_form
from .state import SessionState

def my_login_page()->rx.Component:
    my_child = rx.center(
        rx.cond(
            LoginState.is_hydrated,
            rx.card(login_form()),
        ),
        min_height="89vh",
        padding_top=PADDING_TOP
    )
    return base_page(
        my_child
    )

def my_registration_page()->rx.Component:
    my_child = rx.center(
        rx.cond(
            RegistrationState.success,
            rx.vstack(
                rx.text("Registration successful!"),
            ),
            rx.card(my_register_form()),
        ),
        min_height="89vh",
        padding_top=PADDING_TOP,
    )
    return base_page(
        my_child
    )

def my_logout_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Are you sure you want yo logout?", size="7", text_align="center"),
            rx.link(
                rx.button("No", color_scheme="gray"),
                href=navigation.routes.HOME_ROUTE
            ),
            rx.button("Yes", color_scheme="green", on_click=SessionState.performe_logout),
            #rx.button("About Us",on_click=State.did_click, size="4"),
            spacing="5",
            justify="center",
            align="center",
            text_align="center",
            min_height="89vh",
            id="my_child"
        )

    return base_page(my_child, hide_navbar=False)
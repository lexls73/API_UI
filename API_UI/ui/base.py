import reflex as rx
from ..auth.state import SessionState
from .navbar import navbar
from .dashboard import base_dashboard__page

def base_layout_component(child: rx.Component, *args, **kwargs)-> rx.Component:
    return rx.fragment(
        navbar(),
        rx.box(
            child,
            rx.logo(),
            bg=rx.color("black", 6),
            padding="1em",
            width="100%",
            id="my-base-content_area"
        ),
        id="my-base-container"
    )

def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    return rx.cond(
        SessionState.is_authenticated,
        base_dashboard__page(child, *args, **kwargs),
        base_layout_component(child, *args, **kwargs)
    )
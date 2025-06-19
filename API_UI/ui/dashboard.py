import reflex as rx
from .sidebar import sidebar

def base_dashboard__page(child: rx.Component, *args, **kwargs) -> rx.Component:

    return rx.fragment(
        rx.hstack(
            sidebar(),
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
    )
import reflex as rx
import reflex_local_auth
from reflex.style import toggle_color_mode
from .. import navigation

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/AIZON.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "AIZON", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", navigation.routes.HOME_ROUTE),
                    navbar_link("About", navigation.routes.ABOUT_ROUTE),
                    align_items="center",
                ),
                rx.hstack(
                    rx.link(
                        rx.button(
                            "Login", 
                            size="3",
                            variant="outline"
                        ),
                        href=reflex_local_auth.routes.LOGIN_ROUTE    
                    ),
                    rx.button(
                        rx.color_mode_cond(
                            light=rx.icon("moon"),
                            dark=rx.icon("sun")
                        ),
                        size="3",
                        on_click=toggle_color_mode,
                        variant="outline"
                    ),
                    spacing="4",
                    justify="end"
                ),
                justify="between",
                align_items="center",
                id="my-navbar-hstack-dekstop",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/AIZON.png",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home", on_click=navigation.NavigationState.set_route(navigation.routes.HOME_ROUTE)),
                        rx.menu.item("About", on_click=navigation.NavigationState.set_route(navigation.routes.ABOUT_ROUTE)),
                        rx.menu.separator(),
                        rx.menu.item("Login",on_click=navigation.NavigationState.set_route(reflex_local_auth.routes.LOGIN_ROUTE)),
                        rx.menu.item(rx.color_mode_cond(light=rx.icon("moon"),dark=rx.icon("sun")),on_click=toggle_color_mode)
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        width="100%",
        id="my-main-navbar"
    )

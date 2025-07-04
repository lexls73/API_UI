import reflex as rx
import reflex_local_auth
from ..ui.base import base_page
from . import form

@reflex_local_auth.require_login
def watchdog_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("WatchDog Create Form", size="9", text_align="center"),
            # rx.hstack(
            #     rx.vstack(
            #         rx.list(
            #             rx.list_item("In get mode just pass the ID of the agent to obtain."),
            #             rx.list_item("In create mode, the order of the arguments is: --file_name, --agent_id, --agent_name, --agent_description, --triggering_type,--custom_tags, --profiles, --environment"),
            #             spacing="2"
            #         )
            #     )
            # ),
            rx.desktop_only(
                rx.box(
                    form.form_watchdog_component(),
                    padding="20px",
                    max_width="600px"
                )
            ),
            rx.tablet_only(
                rx.box(
                    form.form_watchdog_component(),
                    padding="20px",
                    width="50vw"
                )
            ),
            rx.mobile_only(
                rx.box(
                    form.form_watchdog_component(),
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
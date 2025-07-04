import reflex as rx
from .state import GetLastValueState

ENVIRONMENTS = ["integration", "appdev", "grifols", "apfc","qa","salessandbox","acssandbox","curia","canary","fis","skbiotek"]
TYPES = ["devices", "elements", "virtual-entities"]
FORMATS = ["csv", "json"]

def form_get_last_component() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.hstack(
                    rx.text("Environment:"),
                    rx.select(
                        ENVIRONMENTS,
                        placeholder="Select the environment",
                        name="environment",
                        value=GetLastValueState.environment,
                        on_change=GetLastValueState.set_environment,
                        flex_grow=1
                    ),
                    width="100%",
                    spacing="2"
                ),
                rx.hstack(
                    rx.text("Entity ID:"),
                    rx.input(
                        placeholder="Entity ID",
                        name="entity_id",
                        value=GetLastValueState.entity_id,
                        on_change=GetLastValueState.set_entity_id,
                        flex_grow=1
                    ),
                    width="100%",
                    spacing="2"
                ),
                rx.hstack(
                    rx.text("Entity Type:"),
                    rx.select(
                        TYPES,
                        placeholder="Entity Type",
                        name="entity_type",
                        value=GetLastValueState.entity_type,
                        on_change=GetLastValueState.set_entity_type,
                        width="100px",
                        flex_grow=1
                    ),
                    width="100%",
                    spacing="2"
                ),
                rx.hstack(
                    rx.text("Format:"),
                    rx.select(
                        FORMATS,
                        placeholder="Select the output format",
                        name="format",
                        value=GetLastValueState.format,
                        on_change=GetLastValueState.set_format,
                        flex_grow=1
                    ),
                    width="100%",
                    spacing="2"
                ),
                rx.hstack(
                    rx.spacer(),
                    rx.vstack(
                        rx.cond(
                                GetLastValueState.is_submitting,
                                rx.spinner(color="blue", size="3"),
                                rx.fragment(),
                            )
                    ),
                    rx.button(
                        "Sent",
                        type="submit",
                        is_loading=GetLastValueState.is_submitting, 
                    ),
                    width="100%",
                    margin_top="2"
                ),
            ),
            on_submit=GetLastValueState.handle_submit,
            width="100%",
            max_width="900px",
            align="center"
        ),
        rx.divider(),
        rx.cond(
            GetLastValueState.data_getting,
            rx.vstack(
                rx.text(f"Selected environment: {GetLastValueState.environment}"),
                rx.text(f"Selected Entity ID: {GetLastValueState.entity_id}"),
                rx.text(f"Selected Entity Type: {GetLastValueState.entity_type}"),
                rx.text(f"Result file: DATA/entities_LastValues.{GetLastValueState.format}"),
            ),
            rx.fragment()
        ),
        width="150%",
        align="start"
    )
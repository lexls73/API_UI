import reflex as rx
from .state import GetDataState

ENVIRONMENTS = ["integration", "appdev", "grifols", "apfc","qa","salessandbox","acssandbox","curia","canary","fis","skbiotek"]
TYPES = ["devices", "elements", "virtual-entities"]
FORMATS = ["csv", "json"]

def form_get_component() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.hstack(
                    rx.text("Environment:"),
                    rx.select(
                        ENVIRONMENTS,
                        placeholder="Select the environment",
                        name="environment",
                        value=GetDataState.environment,
                        on_change=GetDataState.set_environment,
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
                        value=GetDataState.entity_id,
                        on_change=GetDataState.set_entity_id,
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
                        value=GetDataState.entity_type,
                        on_change=GetDataState.set_entity_type,
                        width="100px",
                        flex_grow=1
                    ),
                    width="100%",
                    spacing="2"
                ),
                rx.hstack(
                    rx.text("Start date:"),
                    rx.input(
                        name="start_date",
                        type="datetime-local",
                        value=GetDataState.start_date,
                        on_change=GetDataState.set_start_date,
                        flex_grow=1
                    ),
                    width="100%",
                    spacing="2"
                ),
                rx.hstack(
                    rx.text("End date:"),
                    rx.input(
                        name="end_date",
                        type="datetime-local",
                        value=GetDataState.end_date,
                        on_change=GetDataState.set_end_date,
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
                        value=GetDataState.format,
                        on_change=GetDataState.set_format,
                        flex_grow=1
                    ),
                    width="100%",
                    spacing="2"
                ),
                rx.hstack(
                    rx.spacer(),
                    rx.vstack(
                        rx.cond(
                                GetDataState.is_submitting,
                                rx.spinner(color="blue", size="3"),
                                rx.fragment(),
                            )
                    ),
                    rx.button(
                        "Sent",
                        type="submit",
                        is_loading=GetDataState.is_submitting, 
                    ),
                    width="100%",
                    margin_top="2"
                ),
            ),
            on_submit=GetDataState.handle_submit,
            width="100%",
            max_width="900px",
            align="center"
        ),
        rx.divider(),
        rx.cond(
            GetDataState.data_getting,
            rx.vstack(
                rx.text(f"Selected environment: {GetDataState.environment}"),
                rx.text(f"Selected Entity ID: {GetDataState.entity_id}"),
                rx.text(f"Selected Entity Type: {GetDataState.entity_type}"),
                rx.text(f"Start Date: {GetDataState.start_date}"),
                rx.text(f"End Date: {GetDataState.end_date}"),
                rx.text(f"Result file: DATA/{GetDataState.entity_id}_output.{GetDataState.format}"),
            ),
            rx.fragment()
        ),
        width="150%",
        align="start"
    )
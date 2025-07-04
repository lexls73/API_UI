import reflex as rx
from .state import GetEntitiesState

ENVIRONMENTS = ["integration", "appdev", "grifols", "apfc","qa","salessandbox","acssandbox","curia","canary","fis","skbiotek"]
TYPES = ["devices", "elements", "virtual-entities"]
FORMATS = ["csv", "json"]

def form_component() -> rx.Component:
        return rx.vstack(
        rx.form(
            rx.vstack(
                rx.hstack(
                    rx.text("Environment:"),
                    rx.select(
                        ENVIRONMENTS,
                        placeholder="Select the environment",
                        name="environment",
                        value=GetEntitiesState.environment,
                        on_change=GetEntitiesState.set_environment,
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
                        value=GetEntitiesState.entity_type,
                        on_change=GetEntitiesState.set_entity_type,
                        width="100px",
                        flex_grow=1
                    ),
                    width="100%",
                    spacing="2"
                ),
                rx.hstack(
                    rx.text("Entities ID:"),
                    rx.input(
                        placeholder="Entities ID (Separate with comas)",
                        name="entity_id",
                        #value=GetEntitiesState.entity_id_list,
                        on_change=GetEntitiesState.set_entity_id_selected,
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
                        value=GetEntitiesState.format,
                        on_change=GetEntitiesState.set_format,
                        flex_grow=1
                    ),
                    width="100%",
                    spacing="2"
                ),
                rx.hstack(
                    rx.spacer(),
                    rx.vstack(
                        rx.cond(
                                GetEntitiesState.is_submitting,
                                rx.spinner(color="blue", size="3"),
                                rx.fragment(),
                            )
                    ),
                    rx.button(
                        "Sent",
                        type="submit",
                        is_loading=GetEntitiesState.is_submitting
                    ),
                    width="100%",
                    margin_top="2"
                ),
            ),
            on_submit=GetEntitiesState.handle_submit,
            width="100%",
            max_width="900px",
            align="center"
        ),
        rx.divider(),
        rx.cond(
            GetEntitiesState.data_getting,
            rx.vstack(
                rx.text(f"Selected environment: {GetEntitiesState.environment}"),
                rx.text(f"Selected entity type: {GetEntitiesState.entity_type}"),
                rx.text(f"Selected Entities IDs: {GetEntitiesState.entity_id_selected}"),
                rx.text(f"Result file: DATA/entities_output.{GetEntitiesState.format}"),
            ),
            rx.fragment()
        ),
        width="150%",
        align="start"
    )
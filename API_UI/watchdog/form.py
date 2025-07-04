import reflex as rx
from .state import WatchdogState

ENVIRONMENTS = [
    "integration",
    "appdev",
    "grifols",
    "apfc",
    "qa",
    "salessandbox",
    "acssandbox",
    "curia",
    "canary",
    "fis",
    "skbiotek",
]
TYPES = ["cron", "value"]
FORMATS = ["csv", "json"]
MODES = ["get", "create"]
PATH = "DATA/WATCHDOG/"


def form_watchdog_component() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.hstack(
                    rx.text("Mode:"),
                    rx.select(
                        MODES,
                        placeholder="Select the mode",
                        name="mode",
                        value=WatchdogState.mode,
                        on_change=WatchdogState.set_mode,
                        flex_grow=1,
                    ),
                    width="100%",
                    spacing="2",
                ),
                rx.hstack(
                    rx.text("Environment:"),
                    rx.select(
                        ENVIRONMENTS,
                        placeholder="Select the environment",
                        name="env",
                        value=WatchdogState.environment,
                        on_change=WatchdogState.set_environment,
                        flex_grow=1,
                    ),
                    width="100%",
                    spacing="2",
                ),
                rx.cond(
                    WatchdogState.mode == "",
                    rx.fragment(),
                    rx.cond(
                        WatchdogState.mode == "get",
                        rx.hstack(
                            rx.text("Agent ID:"),
                            rx.input(
                                placeholder="ID of the agent",
                                name="agent_id",
                                value=WatchdogState.agent_id,
                                on_change=WatchdogState.set_agent_id,
                                flex_grow=1,
                            ),
                            width="100%",
                            spacing="2",
                        ),
                        rx.hstack(
                            rx.vstack(
                                rx.hstack(
                                    rx.text("Trigger file Name"),
                                    rx.input(
                                        placeholder="File Name",
                                        name="file_name",
                                        value=WatchdogState.file_name,
                                        on_change=WatchdogState.set_file_name,
                                        flex_grow=1,
                                    ),
                                    width="100%",
                                    spacing="2",
                                ),
                                rx.hstack(
                                    rx.text("Agent ID:"),
                                    rx.input(
                                        placeholder="ID of the agent",
                                        name="agent_id",
                                        value=WatchdogState.agent_id,
                                        on_change=WatchdogState.set_agent_id,
                                        flex_grow=1,
                                    ),
                                    width="100%",
                                    spacing="2",
                                ),
                                rx.hstack(
                                    rx.text("Agent Name:"),
                                    rx.input(
                                        placeholder="Name of the agent",
                                        name="agent_name",
                                        value=WatchdogState.agent_name ,
                                        on_change=WatchdogState.set_agent_name ,
                                        flex_grow=1,
                                    ),
                                    width="100%",
                                    spacing="2",
                                ),
                                rx.hstack(
                                    rx.text("Description:"),
                                    rx.text_area(
                                        placeholder="Agent Description",
                                        name="descripcion",
                                        value=WatchdogState.description,
                                        on_change=WatchdogState.set_description,
                                        width="100%",
                                        min_height="80px"
                                    ),
                                    width="100%",
                                    spacing="2"
                                ),
                                rx.hstack(
                                    rx.text("Triggering Type:"),
                                    rx.select(
                                        TYPES,
                                        placeholder="Select the mode",
                                        name="triggering_type",
                                        value=WatchdogState.triggering_type,
                                        on_change=WatchdogState.set_triggering_type,
                                        flex_grow=1,
                                    ),
                                    width="100%",
                                    spacing="2",
                                ),
                                rx.hstack(
                                    rx.text("Custom Tags:"),
                                    rx.input(
                                        placeholder="Tags separates with commas",
                                        name="custom_tags",
                                        value=WatchdogState.custom_tags ,
                                        on_change=WatchdogState.set_custom_tags ,
                                        flex_grow=1,
                                    ),
                                    width="100%",
                                    spacing="2",
                                ),
                                rx.hstack(
                                    rx.text("Custom Tags:"),
                                    rx.input(
                                        placeholder="Tags separates with commas",
                                        name="custom_tags",
                                        value=WatchdogState.custom_tags ,
                                        on_change=WatchdogState.set_custom_tags ,
                                        flex_grow=1,
                                    ),
                                    width="100%",
                                    spacing="2",
                                ),
                                rx.hstack(
                                    rx.text("Profiles:"),
                                    rx.input(
                                        placeholder="Profiles separates with commas",
                                        name="profiles",
                                        value=WatchdogState.profiles ,
                                        on_change=WatchdogState.set_profiles,
                                        flex_grow=1,
                                    ),
                                    width="100%",
                                    spacing="2",
                                ),
                                rx.hstack(
                                    rx.text("City & Country:"),
                                    rx.input(
                                        placeholder="City & Country separates with commas",
                                        name="city_country",
                                        value=WatchdogState.city_country ,
                                        on_change=WatchdogState.set_city_country,
                                        flex_grow=1,
                                    ),
                                    width="100%",
                                    spacing="2",
                                ),
                            )
                        ),
                    ),
                ),
                rx.hstack(
                    rx.spacer(),
                    rx.vstack(
                        rx.cond(
                            WatchdogState.is_submitting,
                            rx.spinner(color="blue", size="3"),
                            rx.fragment(),
                        )
                    ),
                    rx.button(
                        "Sent",
                        type="submit",
                        is_loading=WatchdogState.is_submitting,
                    ),
                    width="100%",
                    margin_top="2",
                ),
            ),
            on_submit=WatchdogState.handle_submit,
            width="100%",
            max_width="900px",
            align="center",
        ),
        rx.divider(),
        rx.cond(
            WatchdogState.data_getting,
            rx.text(f"Data obtained successfully!"),
            rx.fragment(),
        ),
        width="150%",
        align="start",
    )

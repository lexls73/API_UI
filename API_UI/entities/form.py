import reflex as rx
from .state import EntitiesState

ENVIRONMENTS = ["integration", "appdev", "grifols", "apfc","qa","salesaandbox","acssandbox","curia","canary","fis","skbiotek"]
CONNECTION_MODES = ["insert", "update", "delete"]
MULTI_SELECT_OPTIONS = "devices,elements,virtual-entities,value-associations,associations"

def form_component() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.hstack(
                    # Combo para seleccionar el environment
                    rx.text("Select the environment:"),
                    rx.select(
                        ENVIRONMENTS,
                        placeholder="Select the environment",
                        name="environment",
                        value=EntitiesState.environment,
                        on_change=EntitiesState.set_environment,
                        #width="50%"
                        flex_grow=1 # Hará que ocupe el espacio disponible
                    ),
                    # Input para seleccionar el path de un archivo excel
                    rx.text("Excel file path:"),
                    rx.input(
                        placeholder="Ex: C:/data/mi_file.xlsx",
                        name="excel_path",
                        value=EntitiesState.excel_path,
                        on_change=EntitiesState.set_excel_path,
                        #width="50%"
                        flex_grow=1 # Hará que ocupe el espacio disponible
                    ),
                    width="100%", # Asegura que el hstack ocupe todo el ancho disponible
                    spacing="2" # Agrega espacio entre los elementos si es necesario
                ),
                # Entidades
                rx.text("Entities to be processed (Excel sheets):"),
                rx.text("These are all the options, delete the ones you don't need."),
                rx.text("Separate entities with commas."),
                rx.text("devices,elements,virtual-entities,value-associations,associations"),
                rx.input(
                    name="multi_select",
                    value=MULTI_SELECT_OPTIONS,
                    on_change=EntitiesState.set_selected_options,
                    width="100%"
                ),
                # Combo para seleccionar el modo de conexión
                rx.text("Select the connection mode:"),
                rx.select(
                    CONNECTION_MODES,
                    placeholder="Select the connection mode",
                    name="connection_mode",
                    value=EntitiesState.connection_mode,
                    on_change=EntitiesState.set_connection_mode,
                    width="100%"
                ),
                # Botón submit
                rx.hstack(
                    rx.spacer(),
                    rx.vstack(
                        rx.cond(
                                EntitiesState.is_submitting,
                                rx.spinner(color="blue", size="3"),
                                rx.fragment(),
                            )
                    ),
                    rx.button(
                        "Sent",
                        type="submit",
                        is_loading=EntitiesState.is_submitting, # Deshabilita el botón mientras se envía
                        # Puedes cambiar el texto del botón o ocultarlo si quieres.
                        # Otra opción: poner el spinner al lado del botón o reemplazarlo
                    ),
                    width="100%", # Asegúrate de que el hstack ocupe todo el ancho para que el spacer funcione
                    margin_top="2" # Espacio encima del botón
                ),
            ),
            on_submit=EntitiesState.handle_submit,
            width="90%",
            max_width="900px", # Por ejemplo, no más de 900px de ancho
            align="center"
        ),
        rx.divider(),
        rx.text(f"Selected environment: {EntitiesState.environment}"),
        rx.text(f"Selected Excel Path: {EntitiesState.excel_path}"),
        rx.text(f"Selected entities: {EntitiesState.selected_options}"),
        rx.text(f"Connection mode: {EntitiesState.connection_mode}"),
        width="150%", # o "90%", o "100%" si quieres que abarque todo el ancho.
        # Considera usar 'max_width' si quieres un límite superior
        # para evitar que sea demasiado ancho en pantallas muy grandes.
        #align="center" # Para centrar el vstack si usas un width < "100%"
    )
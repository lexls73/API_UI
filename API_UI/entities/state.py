import reflex as rx
from typing import List
from sqlmodel import select
import bigfinite_api_client as api_client

class EntitiesState(rx.State):
    """Define el estado del formulario."""
    selected_options: str = ""
    excel_path: str = ""
    environment: str = ""
    connection_mode: str = ""
    is_submitting: bool = False
    
    def reset_fields(self):
        self.selected_options = ""
        self.excel_path = ""
        self.environment = ""
        self.connection_mode = ""
        self.is_submitting = False
        yield

    def handle_submit(self, form_data: dict):
        # 1. Mostrar el spinner
        self.is_submitting = True
        yield

        """Maneja el envío del formulario."""
        self.selected_options = form_data.get("multi_select", "")
        self.excel_path = form_data.get("excel_path", "")
        self.environment = form_data.get("environment", "")
        self.connection_mode = form_data.get("connection_mode", "")
        
        entities_list = self.selected_options.split(',')

        # print(f"Opciones seleccionadas: {entities_list}")
        # print(f"Ruta del archivo Excel: {self.excel_path}")
        # print(f"Entorno: {self.environment}")
        # print(f"Modo de conexión: {self.connection_mode}")

        client = api_client.api_helper.get_environment(self.environment)
        
        api_client.api_helper.write_entities_impl(
            api_client=client, mode=self.connection_mode, excel_file=self.excel_path , entity_types=entities_list
        )

        self.is_submitting = False
        yield

        # Aquí podrías añadir la lógica para procesar los datos
        # por ejemplo, conectarse a la base de datos, procesar el Excel, etc.
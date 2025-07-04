import reflex as rx
from typing import List
from sqlmodel import select
from datetime import datetime
import bigfinite_api_client as api_client

class GetEntitiesState(rx.State):
    """Define el estado del formulario."""
    environment:str = ""
    entity_id_selected:str = ""
    entity_type:str = ""
    format:str = ""
    is_submitting: bool = False
    data_getting: bool = False

    def reset_fields(self):
        self.environment = ""
        self.entity_id_selected = ""
        self.entity_type = ""
        self.format = ""
        self.is_submitting = False
        self.data_getting = False
        yield

    def handle_submit(self, form_data: dict):
        # 1. Mostrar el spinner
        self.is_submitting = True
        yield

        """Maneja el envío del formulario."""
        self.environment = form_data.get("environment", "")
        self.entity_id_selected = form_data.get("entity_id", "")
        self.entity_type = form_data.get("entity_type", "")
        self.format = form_data.get("format", "")

        entities_list = self.entity_id_selected.split(',')

        client = api_client.api_helper.get_environment(self.environment)

        if self.entity_type == "devices":
            api_client.api_helper.get_devices_impl(
                client, 
                entities_list,
                self.format, 
                f'DATA/entities_output.{self.format}'
            )
        elif self.entity_type == "elements":
            api_client.api_helper.get_elements_impl(
                client, 
                entities_list,
                self.format, 
                f'DATA/entities_output.{self.format}'
            )
        else:
            api_client.api_helper.get_virtualentities_impl(
                client, 
                entities_list,
                self.format, 
                f'DATA/entities_output.{self.format}'
            )

        self.data_getting = True
        self.is_submitting = False
        yield

        # Aquí podrías añadir la lógica para procesar los datos
        # por ejemplo, conectarse a la base de datos, procesar el Excel, etc.
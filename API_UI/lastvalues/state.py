import reflex as rx
from datetime import datetime
import bigfinite_api_client as api_client

class GetLastValueState(rx.State):
    """Define el estado del formulario."""
    environment: str = ""
    entity_id: str = ""
    entity_type = ""
    format: str = ""
    is_submitting: bool = False
    data_getting: bool = False

    def reset_fields(self):
        self.environment = ""
        self.entity_id = ""
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
        self.entity_id = form_data.get("entity_id", "")
        self.entity_type = form_data.get("entity_type", "")
        
        entities_list = self.entity_id .split(',')

        client = api_client.api_helper.get_environment(self.environment)

        if self.entity_type == "devices":
            api_client.api_helper.get_device_lastvalues_impl(client,
                                                            entities_list,
                                                            self.format,
                                                            f'DATA/entities_LastValues.{self.format}')
        elif self.entity_type == "elements":
            api_client.api_helper.get_element_lastvalues_impl(client,
                                                            entities_list,
                                                            self.format,
                                                            f'DATA/entities_LastValues.{self.format}')
        else:
            api_client.api_helper.get_virtualentities_lastvalues_impl(client,
                                                                    entities_list,
                                                                    self.format,
                                                                    f'DATA/entities_LastValues.{self.format}')
        self.data_getting = True
        self.is_submitting = False
        yield
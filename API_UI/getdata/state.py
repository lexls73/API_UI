import reflex as rx
from datetime import datetime
import bigfinite_api_client as api_client

class GetDataState(rx.State):
    """Define el estado del formulario."""
    environment: str = ""
    entity_id: str = ""
    entity_id_list:list = []
    entity_type: str = ""
    start_date: str = ""
    end_date: str = ""
    format: str = ""
    is_submitting: bool = False
    data_getting: bool = False
    
    @staticmethod
    def date_to_iso(date_str: str) -> str:
        """Convierte 'YYYY-MM-DD' a ISO 8601 con hora de inicio o fin del día."""
        if not date_str:
            return ""
        
        dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M")
        return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
    def reset_fields(self):
        self.environment = ""
        self.entity_id = ""
        self.entity_id_list = []
        self.entity_type = ""
        self.start_date = ""
        self.end_date = ""
        self.format = ""
        self.is_submitting = False
        self.data_getting = False
        yield

    def handle_submit(self, form_data: dict):
        pass
        # 1. Mostrar el spinner
        self.is_submitting = True
        yield

        """Maneja el envío del formulario."""
        self.environment = form_data.get("environment", "")
        self.entity_id = form_data.get("entity_id", "")
        self.entity_type = form_data.get("entity_type", "")
        self.start_date = form_data.get("start_date", "")
        self.end_date = form_data.get("end_date", "")
        self.format = form_data.get("format", "")
        
        self.entity_id_list.append(self.entity_id)

        start_iso = self.date_to_iso(self.start_date)
        end_iso = self.date_to_iso(self.end_date)
        
        #print(f'DATA/{self.entity_id}_output.{self.format}')

        client = api_client.api_helper.get_environment(self.environment)
        
        if self.entity_type == "devices":
            api_client.api_helper.get_device_timeseries_impl(client,
                                                            start_iso,
                                                            end_iso,
                                                            self.entity_id_list,
                                                            self.format,
                                                            f'DATA/{self.entity_id}_output.{self.format}')
        elif self.entity_type == "elements":
            api_client.api_helper.get_element_timeseries_impl(client,
                                                            start_iso,
                                                            end_iso,
                                                            self.entity_id_list,
                                                            self.format,
                                                            f'DATA/{self.entity_id}_output.{self.format}')
        else:
            api_client.api_helper.get_virtualentity_timeseries_impl(client,
                                                                    start_iso,
                                                                    end_iso,
                                                                    self.entity_id_list,
                                                                    self.format,
                                                                    f'DATA/{self.entity_id}_output.{self.format}')
        self.data_getting = True
        self.is_submitting = False
        yield
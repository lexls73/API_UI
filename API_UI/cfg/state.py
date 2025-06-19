import reflex as rx
from ..auth.state import SessionState
import configparser
from pathlib import Path

CFG_PATH = Path.home() / ".config/BigfiniteAPIClient/bigfinite_api_client.cfg"

class BigfiniteCfgState(rx.State):
    config_data: dict = {}
    section: str = ""
    user: str = ""
    customer: str = ""
    password: str = ""
    success_msg: str = "" 
    cfg_path: str = CFG_PATH
    load_ok :bool = False
    is_loading: bool = False
    
    def set_section(self, value):
        self.section = value
        # Al seleccionar una sección, actualiza automáticamente el customer
        self.customer = self.config_data.get(value, {}).get("customer", "")
        
    def reset_fields(self):
        self.section = ""
        self.user = ""
        self.customer = ""
        self.password = ""
        self.success_msg = ""
        self.config_data = {}
        self.load_ok = False
        is_loading: bool = False
        yield

    def load_config(self):
        self.is_loading = True
        yield
        parser = configparser.ConfigParser(interpolation=None)
        parser.read(CFG_PATH)
        self.config_data = {s: dict(parser.items(s)) for s in parser.sections()}
        self.success_msg = ""
        self.load_ok = True
        self.is_loading = False
        yield

    def save_section(self, form_data: dict):
        self.is_loading = True
        yield
        parser = configparser.ConfigParser(interpolation=None)
        parser.read(CFG_PATH)
        parser[self.section] = {
            "user": form_data.get("user",""),
            "customer": self.customer,
            "password": self.password,
        }
        with open(CFG_PATH, "w") as f:
            parser.write(f)
        self.load_config()
        # Limpiar los campos del formulario
        self.section = ""
        self.user = ""
        self.customer = ""
        self.password = ""
        self.success_msg = "Config saved successfully!" 
        self.is_loading = False
        yield
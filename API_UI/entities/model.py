
import reflex as rx
from sqlmodel import Field

class EntityModel(rx.Model, table=True):
    entity_id: int = Field(nullable=True)
    enttity_name: str 
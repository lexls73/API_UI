
import reflex as rx
import sqlalchemy
from sqlmodel import Field
from datetime import datetime
from .. import utils

class ConctacEntryModel(rx.Model, table=True):
    user_id: int = Field(nullable=True)
    first_name: str 
    last_name: str = Field(nullable=True)
    email: str = Field(nullable=True)
    message: str
    created_at: datetime = Field(
        default_factory= utils.timing.get_utc_now, #lambda: datetime.now(timezone.utc),
        sa_type=sqlalchemy.DATETIME(timezone=True),
        sa_column_kwargs={
            "server_default": sqlalchemy.func.now()
        },
        nullable=False
    )
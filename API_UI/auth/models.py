import reflex as rx
from reflex_local_auth.user import LocalUser
from sqlmodel import Field, Relationship
import sqlalchemy
from datetime import datetime
from .. import utils

class UserInfo(rx.Model, table=True):
    email:str
    user_id:int = Field(foreign_key='localuser.id')
    user: LocalUser | None = Relationship()
    created_at: datetime = Field(
        default_factory= utils.timing.get_utc_now, #lambda: datetime.now(timezone.utc),
        sa_type=sqlalchemy.DATETIME(timezone=True),
        sa_column_kwargs={
            "server_default": sqlalchemy.func.now()
        },
        nullable=False
    )
    updated_at: datetime = Field(
        default_factory= utils.timing.get_utc_now, #lambda: datetime.now(timezone.utc),
        sa_type=sqlalchemy.DATETIME(timezone=True),
        sa_column_kwargs={
            "onupdate": sqlalchemy.func.now(),
            "server_default": sqlalchemy.func.now()
        },
        nullable=False
    )
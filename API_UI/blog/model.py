import reflex as rx
import sqlalchemy
from sqlmodel import Field
from datetime import datetime
from .. import utils

class BlogPostModel(rx.Model, table=True):
    #blog_post_id: int = Field(nullable=True)
    title: str
    content: str
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
    #published_date:
    #published_time:
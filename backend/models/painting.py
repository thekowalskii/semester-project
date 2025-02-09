from enum import Enum as stdEnum
import uuid

from sqlalchemy import String, Enum as saEnum
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import PGBase
from backend.api.dependencies.db import Session_dp
from backend.schemas import PaintingSchemaFull, PaintingSchema
from backend.databases.redis_manager import redis_manager


class Painting(PGBase):
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    available: Mapped[int] = mapped_column()
    

    @classmethod
    async def create(cls, session: Session_dp, painting: PaintingSchemaFull):
        new = cls(
            title=painting.title,
            description=painting.description,
            price=painting.price,
            available=painting.available
        )

        session.add(new)
        await session.commit()

        # adding this photo into Redis

        redis_manager.add_photo(
            title=new.title,
            photo=painting.hex_photo
        )

        return None
    
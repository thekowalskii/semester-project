from enum import Enum as stdEnum
import uuid

from sqlalchemy import String, Enum as saEnum
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import PGBase
from backend.api.dependencies.db import Session_dp
from backend.schemas.picture import PictureSchemaFull, PictureSchema
from backend.databases.redis_manager import redis_manager


class Picture(PGBase):
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    

    @classmethod
    async def create(cls, session: Session_dp, picture: PictureSchemaFull):
        new = cls(
            title=picture.title,
            description=picture.description,
            price=picture.price
        )

        session.add(new)
        await session.commit()

        # adding this photo into Redis

        redis_manager.add_photo(
            title=new.title,
            photo=picture.hex_photo
        )

        return None
    
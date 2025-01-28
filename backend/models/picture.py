from enum import Enum as stdEnum

from sqlalchemy import String, Enum as saEnum
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import PGBase


class Picture(PGBase):
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    redis_id: Mapped[int] = mapped_column()
    

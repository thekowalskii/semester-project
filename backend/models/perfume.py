from enum import Enum as stdEnum
import uuid

from sqlalchemy import String, Enum as saEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.product_base import ProductBase


class Perfume(ProductBase):
    id: Mapped[uuid.UUID] = mapped_column(ForeignKey('productbases.id'), primary_key=True)

    volume: Mapped[int] = mapped_column()
    description: Mapped[str] = mapped_column()
    available: Mapped[int] = mapped_column()

    first_notes: Mapped[str] = mapped_column()
    perfume_heart: Mapped[str] = mapped_column()
    last_notes: Mapped[str] = mapped_column()

    __mapper_args__ = {
        'polymorphic_identity': 'perfume'
    }

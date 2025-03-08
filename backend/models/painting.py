from enum import Enum as stdEnum
import uuid

from sqlalchemy import String, Enum as saEnum, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.product_base import ProductBase
from .enums.painting import PaintingOrientationEnum


class Painting(ProductBase):
    id: Mapped[uuid.UUID] = mapped_column(ForeignKey('productbases.id'), primary_key=True)

    description: Mapped[str] = mapped_column()
    
    width: Mapped[float] = mapped_column()
    height: Mapped[float] = mapped_column()
    orientation: Mapped[PaintingOrientationEnum] = mapped_column(saEnum(PaintingOrientationEnum, name='painting_orientation'))

    __mapper_args__ = {
        'polymorphic_identity': 'painting',
    }

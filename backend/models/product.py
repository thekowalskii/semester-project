from enum import Enum as stdEnum
import uuid

from sqlalchemy import String, Enum as saEnum, ARRAY, String, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.product_base import ProductBase, ProductsMethods


class Product(ProductsMethods, ProductBase):
    id: Mapped[uuid.UUID] = mapped_column(ForeignKey('productbases.id'), primary_key=True)

    description: Mapped[str] = mapped_column()
    materials: Mapped[list[str]] = mapped_column(ARRAY(String))
    width: Mapped[float] = mapped_column()
    height: Mapped[float] = mapped_column()

    __mapper_args__ = {
        'polymorphic_identity': 'product'
    }

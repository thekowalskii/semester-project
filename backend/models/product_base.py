from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import PGBase


class ProductBase(PGBase):
    # __tablename__ = 'product_base'
    __table_args__ = {
        'extend_existing': True
    }

    title: Mapped[str] = mapped_column(unique=True)
    price: Mapped[int] = mapped_column()
    type: Mapped[str] = mapped_column()
    
    __mapper_args__ = {
        "polymorphic_identity": "product_base",
        "polymorphic_on": type
    }

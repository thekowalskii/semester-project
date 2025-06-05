from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as saEnum

from backend.models.base import PGBase
from backend.api.dependencies.db import Session_dp
from backend.databases.redis_manager import redis_manager
from backend.schemas import PriceCurrencyEnum


class ProductBase(PGBase):
    # __tablename__ = 'product_base'
    __table_args__ = {
        'extend_existing': True
    }

    title: Mapped[str] = mapped_column(unique=True)
    price: Mapped[int] = mapped_column()
    currency: Mapped[PriceCurrencyEnum] = mapped_column(saEnum(PriceCurrencyEnum, name='price_currency'))
    type: Mapped[str] = mapped_column()
    
    __mapper_args__ = {
        "polymorphic_identity": "product_base",
        "polymorphic_on": type
    }


class ProductsMethods:

    '''
    All the goods, such as paintings, perfumes and products,
    have some similar methods, so i placed those methods here, 
    to keep my code clear and to not repeat myself
    '''

    @classmethod
    async def create(cls, session: Session_dp, photo_in_hex, **kwargs):
        instance = cls(**kwargs)

        session.add(instance)
        await session.commit()

        await redis_manager.add_photo(
            title=instance.title,
            photo=photo_in_hex,
        )

        return instance

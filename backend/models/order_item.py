from enum import Enum as stdEnum
import uuid

from sqlalchemy import String, Enum as saEnum, Integer, ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import PGBase
from backend.api.dependencies.db import Session_dp
from .painting import Painting


class OrderItem(PGBase):
    __tablename__ = 'order_items'
    
    product_title: Mapped[str] = mapped_column()
    product_description: Mapped[str] = mapped_column()
    product_price: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()

    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('paintings.id'))
    order_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('orders.id'))

    product = relationship('Painting')
    order: Mapped['Order'] = relationship('Order', back_populates='order_items', lazy='joined')


    @classmethod
    async def create(cls, session: Session_dp, product_id, quantity, order):
        painting = await session.execute(select(Painting).where(Painting.id == product_id))
        painting = painting.scalars().one()

        new = OrderItem(
            product_price=painting.price,
            quantity=quantity,
            product_id=product_id,
            order_id=order.id,
            product=painting,
            order=order,
            product_title=painting.title,
            product_description=painting.description
        )

        session.add(new)
        await session.commit()

        return painting.title


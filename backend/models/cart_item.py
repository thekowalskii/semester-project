import uuid

from sqlalchemy import Enum as ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import PGBase
from backend.api.dependencies.db import Session_dp
from .painting import Painting


class CartItem(PGBase):
    __tablename__ = 'cart_items'
    
    product_price: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()

    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('paintings.id'))
    cart_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('carts.id'))

    product = relationship('Painting')
    cart: Mapped['Cart'] = relationship('Cart', back_populates='cart_items', lazy='joined')


    @classmethod
    async def create(cls, session: Session_dp, product_id, quantity, cart):
        painting = await session.execute(select(Painting).where(Painting.id == product_id))
        painting = painting.scalars().one()

        new = CartItem(
            product_price=painting.price,
            quantity=quantity,
            product_id=product_id,
            cart_id=cart.id,
            product=painting,
            cart=cart,
        )

        session.add(new)
        await session.commit()

        return painting.title

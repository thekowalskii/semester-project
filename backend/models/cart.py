from datetime import date

from sqlalchemy import Enum , Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import PGBase
from backend.api.dependencies.db import Session_dp
from .cart_item import CartItem


class Cart(PGBase):
    total_price: Mapped[int] = mapped_column()
    status: Mapped[str] = mapped_column(Enum('forming', 'waiting for accept', 'accepted', name='cart_status_enum'))
    created_at: Mapped[date] = mapped_column(Date, default=date.today)

    cart_items: Mapped[list["CartItem"]] = relationship(
        back_populates="cart", cascade="all, delete-orphan", lazy="joined"
    )

    def update_total_price(self):
        total_price = 0

        for product in self.cart_items:
            total_price += product.product_price * product.quantity

        self.total_price = total_price

        return


    @classmethod
    async def create(cls, session: Session_dp):
        new = cls(
            total_price=0,
            status='forming'
        )

        session.add(new)
        await session.commit()

        return new

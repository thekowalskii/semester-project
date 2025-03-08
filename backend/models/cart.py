from datetime import date

from sqlalchemy import Enum as saEnum, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import PGBase
from .enums.cart import CartStatusEnum


class Cart(PGBase):
    total_price: Mapped[int] = mapped_column(default=0)
    status: Mapped[CartStatusEnum] = mapped_column(saEnum(CartStatusEnum, name='cart_status'), default=CartStatusEnum.forming)
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

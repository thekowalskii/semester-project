from datetime import date

from sqlalchemy import Enum as saEnum, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import PGBase
from backend.schemas import OrderStatusEnum


class Order(PGBase):
    total_price: Mapped[int] = mapped_column(default=0)
    status: Mapped[OrderStatusEnum] = mapped_column(saEnum(OrderStatusEnum, name='order_status'), default=OrderStatusEnum.forming)
    created_at: Mapped[date] = mapped_column(Date, default=date.today)

    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order", cascade="all, delete-orphan", lazy="joined"
    )


    def update_total_price(self):
        total_price = 0

        for product in self.order_items:
            total_price += product.product_price * product.quantity

        self.total_price = total_price

        return

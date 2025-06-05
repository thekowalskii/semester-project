from typing import Optional

from pydantic import BaseModel
from fastapi import Form

from .enums.currency import PriceCurrencyEnum


class ProductBaseSchema(BaseModel):
    title: str
    description: Optional[str] = Form(None)
    price: int
    currency: PriceCurrencyEnum

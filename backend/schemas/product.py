from typing import List

from pydantic import field_validator
from fastapi import Form

from .product_base import ProductBaseSchema
from .enums.currency import PriceCurrencyEnum


class ProductSchema(ProductBaseSchema):
    '''
    In such form admin should provide data to create new product
    '''
    materials: List[str]
    width: float
    height: float
    

    @field_validator('description')
    def validate_description(v):
        if v == '':
            v = 'Description is empty.'

        return v


def parse_product(
    title: str = Form(...),
    description: str | None = Form(None),
    price: int = Form(...),
    currency: PriceCurrencyEnum = Form(...),
    materials: List[str] = Form(...),
    width: float = Form(...),
    height: float = Form(...),
) -> ProductSchema:
        return ProductSchema(title=title, description=description, price=price, 
                            currency=currency, materials=materials, width=width, 
                            height=height
                            )


class ProductSchemaFull(ProductSchema):
    '''
    In such form database receive new product
    '''

    hex_photo: str

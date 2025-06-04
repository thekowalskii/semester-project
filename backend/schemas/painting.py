from pydantic import field_validator
from fastapi import Form

from .enums.painting import PaintingOrientationEnum
from .product_base import ProductBaseSchema
from .enums.currency import PriceCurrencyEnum


class PaintingSchema(ProductBaseSchema):
    '''
    In such form admin should provide data to create new painting
    '''
    width: float
    height: float
    orientation: str

    @field_validator('description')
    def validate_description(v):
        if v == '':
            v = 'Description is empty.'

        return v


def parse_painting(
    title: str = Form(...),
    description: str | None = Form(None),
    price: int = Form(...),
    currency: PriceCurrencyEnum = Form(...),
    available: int = Form(...),
    width: float = Form(...),
    height: float = Form(...),
    orientation: PaintingOrientationEnum = Form(...)
) -> PaintingSchema:
    return PaintingSchema(title=title, description=description, price=price, currency=currency,
                          available=available, width=width, height=height, orientation=orientation)


class PaintingSchemaFull(PaintingSchema):
    '''
    In such form database receive new painting
    '''

    hex_photo: str

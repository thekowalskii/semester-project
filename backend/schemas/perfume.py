from pydantic import field_validator
from fastapi import Form

from .product_base import ProductBaseSchema
from .enums.currency import PriceCurrencyEnum


class PerfumeSchema(ProductBaseSchema):
    '''
    In such form admin should provide data to create new perfume
    '''
    available: int
    volume: float
    first_notes: str
    perfume_heart: str
    last_notes: str

    model_config = {
        'from_attributes': True
    }

    @field_validator('description')
    def validate_description(v):
        if v == '':
            v = 'Description is empty.'

        return v


def parse_perfume(
    title: str = Form(...),
    description: str | None = Form(None),
    price: int = Form(...),
    currency: PriceCurrencyEnum = Form(...),
    volume: float = Form(...),
    available: int = Form(...),
    first_notes: str = Form(...),
    perfume_heart: str = Form(...),
    last_notes: str = Form(...),
) -> PerfumeSchema:
    return PerfumeSchema(title=title, description=description, price=price, currency=currency,
                          volume=volume, available=available, first_notes=first_notes, 
                          perfume_heart=perfume_heart, last_notes=last_notes
                        )


class PerfumeSchemaFull(PerfumeSchema):
    '''
    In such form database receive new perfume
    '''

    hex_photo: str

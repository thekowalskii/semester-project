from typing import Optional

from pydantic import BaseModel, field_validator
from fastapi import Form


class PerfumeSchema(BaseModel):
    '''
    In such form admin should provide data to create new perfume
    '''
    title: str
    description: str = Form('')
    price: int
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
    volume: float = Form(...),
    available: int = Form(...),
    first_notes: str = Form(...),
    perfume_heart: str = Form(...),
    last_notes: str = Form(...),
) -> PerfumeSchema:
    return PerfumeSchema(title=title, description=description, price=price, 
                          volume=volume, available=available, first_notes=first_notes, 
                          perfume_heart=perfume_heart, last_notes=last_notes
                        )


class PerfumeSchemaFull(PerfumeSchema):
    '''
    In such form database receive new perfume
    '''

    hex_photo: str

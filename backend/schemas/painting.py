from typing import Optional

from pydantic import BaseModel, field_validator
from fastapi import Form

from .user import UserSchema, UserResponseSchema
from .enums.painting import PaintingOrientationEnum


class PaintingSchema(BaseModel):
    '''
    In such form admin should provide data to create new painting
    '''
    title: str
    description: Optional[str] = Form(None)
    price: int
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
    available: int = Form(...),
    width: float = Form(...),
    height: float = Form(...),
    orientation: PaintingOrientationEnum = Form(...)
) -> PaintingSchema:
    return PaintingSchema(title=title, description=description, price=price, 
                          available=available, width=width, height=height, orientation=orientation)


class PaintingSchemaFull(PaintingSchema):
    '''
    In such form database receive new painting
    '''

    hex_photo: str

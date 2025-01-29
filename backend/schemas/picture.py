from typing import Annotated, Optional
import uuid

from pydantic import BaseModel, field_validator
from fastapi import UploadFile, File, Form


class HashSchema(BaseModel):
    hashed: Annotated[bytes, File(...)]


class PictureSchema(BaseModel):
    '''
    In such form admin should provide data to create new picture
    '''
    title: str
    description: Optional[str] = Form(None)
    price: int


    @field_validator('description')
    def validate_description(v):
        if v == '':
            v = 'Description is empty.'

        return v


def parse_picture(
    title: str = Form(...),
    description: str | None = Form(None),
    price: int = Form(...)
) -> PictureSchema:
    return PictureSchema(title=title, description=description, price=price)


class PictureSchemaFull(PictureSchema):
    '''
    In such form database receive new picture
    '''

    hex_photo: str

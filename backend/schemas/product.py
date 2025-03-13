from typing import Optional, List

from pydantic import BaseModel, field_validator
from fastapi import Form


class ProductSchema(BaseModel):
    '''
    In such form admin should provide data to create new product
    '''
    title: str
    description: Optional[str] = Form(None)
    price: int
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
    materials: List[str] = Form(...),
    width: float = Form(...),
    height: float = Form(...),
) -> ProductSchema:
    return ProductSchema(title=title, description=description, price=price, 
                          materials=materials, width=width, height=height
                        )


class ProductSchemaFull(ProductSchema):
    '''
    In such form database receive new product
    '''

    hex_photo: str

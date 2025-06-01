import uuid

from fastapi import APIRouter, Request, Depends, UploadFile, File
from fastapi.responses import StreamingResponse

from backend.api.dependencies.db import Session_dp
from backend.api.dependencies.scope import admin_scope_dp
from backend.schemas import ProductSchema, parse_product
from backend.databases.redis_manager import redis_manager
from backend.models.product import Product
from backend.services import hex_to_image


products_r = APIRouter(tags=['products'], prefix='/products')


@products_r.post('/create', dependencies=[admin_scope_dp])
async def create_product(request: Request, 
                         session: Session_dp,
                         painting: UploadFile = File(...),
                         form_data: ProductSchema = Depends(parse_product)
):

    photo_in_hex = await painting.read()
    photo_in_hex = photo_in_hex.hex()

    painting = await Product.create(
        session=session,
        photo_in_hex=photo_in_hex,
        title=form_data.title,
        price=form_data.price,
        description=form_data.description,
        width=form_data.width,
        height=form_data.height,
        materials=form_data.materials
    )

    return 'created'


@products_r.get('/get_one')
async def get_product_photo(request: Request, session: Session_dp, title: str):
    title = title.replace('_', ' ')

    painting = await Product.get(
        session=session, 
        field=Product.title, 
        value=title
    )

    image = await redis_manager.get_photo(title=painting.title)
    image = hex_to_image(image)

    return StreamingResponse(content=image, media_type='image/png')


@products_r.get('/get_all')
async def get_all(request: Request, session: Session_dp):
    products = await Product.all(session=session)

    res = [{
        'title': p.title,
        'title_wos': p.title.replace(' ', '_'),
        'description': p.description,
        'price': p.price,
        'width': p.width,
        'height': p.height,
        'materials': p.materials
    } for p in products]

    return res


@products_r.delete('/delete')
async def delete(session: Session_dp, id: uuid.UUID):
    await Product.delete(session=session, id=id)

    return 204

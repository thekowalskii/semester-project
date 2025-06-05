import uuid

from fastapi import APIRouter, Request, Depends, UploadFile, File, Query
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
        currency=form_data.currency,
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
        'title_wos': p.title.replace(' ', '_'), # "wos" - means "without spaces", so all the spaces are replaced with underscore
        'description': p.description,
        'short_description': p.description if len(p.description) <= 23 else p.description[0:20] + '...',
        'price': p.price,
        'currency': p.currency,
        'width': p.width,
        'height': p.height,
        'materials': p.materials
    } for p in products]

    return res


@products_r.delete('/delete')
async def delete(session: Session_dp, id: uuid.UUID):
    await Product.delete(session=session, id=id)

    return 204


@products_r.get('/info')
async def get_info(request: Request, session: Session_dp, id: uuid.UUID = Query(...)):
    product = await Product.get(session=session, field=Product.id, value=id)

    return {
        'id': product.id,
        'title': product.title,
        'title': product.title,
        'title_wos': product.title.replace(' ', '_'), # "wos" - means "without spaces", so all the spaces are replaced with underscore
        'description': product.description,
        'short_description': product.description if len(product.description) <= 23 else product.description[0:20] + '...',
        'price': product.price,
        'currency': product.currency,
        'materials': product.materials,
        'width': product.width,
        'height': product.height
    }

import uuid

from fastapi import APIRouter, Request, Depends, UploadFile, File, Header
from fastapi.responses import StreamingResponse

from backend.api.dependencies.db import Session_dp
from backend.api.dependencies.scope import admin_scope_dp
from backend.schemas import PaintingSchema, parse_painting
from backend.databases.redis_manager import redis_manager
from backend.models.painting import Painting
from backend.services import hex_to_image


painting_r = APIRouter(tags=['paintings'], prefix='/paintings')


@painting_r.post('/create', dependencies=[admin_scope_dp])
async def create_painting(request: Request, 
                         session: Session_dp,
                         painting: UploadFile = File(...),
                         form_data: PaintingSchema = Depends(parse_painting)
):

    photo_in_hex = await painting.read()
    photo_in_hex = photo_in_hex.hex()

    painting = await Painting.create(
        session=session,
        photo_in_hex=photo_in_hex,
        title=form_data.title,
        price=form_data.price,
        description=form_data.description,
        width=form_data.width,
        height=form_data.height,
        orientation=form_data.orientation
    )

    return 'created'


@painting_r.get('/get_one')
async def get_product_photo(request: Request, session: Session_dp, title: str):
    title = title.replace('_', ' ')

    painting = await Painting.get(
        session=session, 
        field=Painting.title, 
        value=title
    )

    image = await redis_manager.get_photo(title=painting.title)
    image = hex_to_image(image)

    return StreamingResponse(content=image, media_type='image/png')


@painting_r.get('/get_all')
async def get_all(request: Request, session: Session_dp):
    products = await Painting.all(session=session)

    res = [{
        'title': p.title,
        'title_wos': p.title.replace(' ', '_'),
        'description': p.description,
        'short_description': p.description if len(p.description) <= 23 else p.description[0:20] + '...',
        'price': p.price,
        'width': p.width,
        'height': p.height,
        'orientation': p.orientation
    } for p in products]

    return res


@painting_r.delete('/delete')
async def delete(session: Session_dp, id: uuid.UUID):
    await Painting.delete(session=session, id=id)

    return 204

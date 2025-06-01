import uuid

from fastapi import APIRouter, Request, Depends, UploadFile, File
from fastapi.responses import StreamingResponse

from backend.api.dependencies.db import Session_dp
from backend.api.dependencies.scope import admin_scope_dp
from backend.schemas import PerfumeSchema, parse_perfume
from backend.databases.redis_manager import redis_manager
from backend.models import Perfume
from backend.services import hex_to_image


perfumes_r = APIRouter(tags=['perfumes'], prefix='/perfumes')


@perfumes_r.post('/create', dependencies=[admin_scope_dp])
async def create_perfume(request: Request, 
                         session: Session_dp,
                         painting: UploadFile = File(...),
                         form_data: PerfumeSchema = Depends(parse_perfume)
):

    photo_in_hex = await painting.read()
    photo_in_hex = photo_in_hex.hex()

    painting = await Perfume.create(
        session=session,
        photo_in_hex=photo_in_hex,
        title=form_data.title,
        description=form_data.description,
        price=form_data.price,
        available=form_data.available,
        volume=form_data.volume,
        first_notes=form_data.first_notes,
        perfume_heart=form_data.perfume_heart,
        last_notes=form_data.last_notes,
    )

    return 'created'


@perfumes_r.get('/get_one')
async def get_product_photo(request: Request, session: Session_dp, title: str):
    title = title.replace('_', ' ')

    perfume = await Perfume.get(
        session=session, 
        field=Perfume.title, 
        value=title
    )

    image = await redis_manager.get_photo(title=perfume.title)
    image = hex_to_image(image)

    return StreamingResponse(image, media_type='image/png')


@perfumes_r.get('/get_all')
async def get_all(request: Request, session: Session_dp):
    products = await Perfume.all(session=session)

    res = [{
        'title': p.title,
        'title_wos': p.title.replace(' ', '_'),
        'description': p.description,
        'price': p.price,
        'available': p.available,
        'volume': p.volume,
        'first_notes': p.first_notes,
        'perfume_heart': p.perfume_heart,
        'last_notes': p.last_notes,
    } for p in products]

    return res


@perfumes_r.delete('/delete')
async def delete(session: Session_dp, id: uuid.UUID):
    await Perfume.delete(session=session, id=id)

    return 204

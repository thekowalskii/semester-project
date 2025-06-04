import uuid

from fastapi import APIRouter, Request, Depends, UploadFile, File, Query
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
        currency=form_data.currency,
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
        'title_wos': p.title.replace(' ', '_'), # "wos" - means "without spaces", so all the spaces are replaced with underscore
        'description': p.description,
        'short_description': p.description if len(p.description) <= 23 else p.description[0:20] + '...',
        'price': p.price,
        'currency': p.currency,
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


@perfumes_r.get('/info')
async def get_info(request: Request, session: Session_dp, id: uuid.UUID = Query(...)):
    perfume = await Perfume.get(session=session, field=Perfume.id, value=id)

    return {
        'id': perfume.id,
        'title': perfume.title,
        'title': perfume.title,
        'title_wos': perfume.title.replace(' ', '_'), # "wos" - means "without spaces", so all the spaces are replaced with underscore
        'description': perfume.description,
        'short_description': perfume.description if len(perfume.description) <= 23 else perfume.description[0:20] + '...',
        'price': perfume.price,
        'currency': perfume.currency,
        'first_notes': perfume.first_notes,
        'perfume_heart': perfume.perfume_heart,
        'last_notes': perfume.last_notes,
        'available': perfume.available,
        'volume': perfume.volume,
    }

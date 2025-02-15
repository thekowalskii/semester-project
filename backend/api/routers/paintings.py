import time
import asyncio
import uuid

from fastapi import APIRouter, Request, Depends, UploadFile, File
from fastapi.responses import StreamingResponse

from backend.api.dependencies.db import Session_dp
from backend.api.dependencies.scope import admin_scope_dp
from backend.schemas import PaintingSchema, PaintingSchemaFull, parse_painting
from backend.databases.redis_manager import redis_manager
from backend.models.painting import Painting
from backend.utils import password_manager
from backend.services import token_manager, hex_to_image, hex_to_base64


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
        painting=PaintingSchemaFull(
            **form_data.model_dump(), 
            hex_photo=photo_in_hex
            )
    )

    return 'created'


@painting_r.delete('/delete')
async def delete(session: Session_dp, id: uuid.UUID):
    await Painting.delete(session=session, id=id)

    return 204


@painting_r.get('/get_one')
async def get_product_photo(request: Request, session: Session_dp, title: str):
    painting = await Painting.get(
        session=session, 
        field=Painting.title, 
        value=title
    )

    image = await redis_manager.get_photo(title=painting.title)
    image = hex_to_image(image)

    return StreamingResponse(image, media_type='image/png')


@painting_r.get('/get_all')
async def get_all(request: Request, session: Session_dp):
    products = await Painting.all(session=session)

    res = [{
        'title': p.title,
        'description': p.description,
        'price': p.price
    } for p in products]

    return res

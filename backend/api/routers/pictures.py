import time

from fastapi import APIRouter, Request, Response, Depends, HTTPException, status, UploadFile, File
from starlette.responses import FileResponse
from fastapi.responses import StreamingResponse

from backend.api.dependencies.db import Session_dp
from backend.api.dependencies.scope import admin_scope_dp
from backend.schemas.picture import PictureSchema, PictureSchemaFull, parse_picture
from backend.databases.redis_manager import redis_manager
from backend.models.picture import Picture
from backend.utils import password_manager
from backend.services import token_manager, hex_to_image


pictures_r = APIRouter(tags=['pictures'])


@pictures_r.post('/create_picture', dependencies=[admin_scope_dp])
async def create_picture(request: Request, 
                         session: Session_dp,
                         picture: UploadFile = File(...),
                         form_data: PictureSchema = Depends(parse_picture)
):

    photo_in_hex = await picture.read()
    photo_in_hex = photo_in_hex.hex()

    picture = await Picture.create(
        session=session, 
        picture=PictureSchemaFull(
            **form_data.model_dump(), 
            hex_photo=photo_in_hex
            )
    )

    return 'created'


@pictures_r.get('/get_photo')
async def get_photo(request: Request, session: Session_dp, title: str):
    picture = await Picture.get(
        session=session, 
        field=Picture.title, 
        value=title
    )

    image = redis_manager.get_photo(title=picture.title)
    image = hex_to_image(image)

    return StreamingResponse(image, media_type='image/png')

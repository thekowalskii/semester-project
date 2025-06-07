from fastapi import APIRouter


ukr_r = APIRouter(
    tags=['UKR'],
    prefix='/ukr'
)


@ukr_r.get('/get/localities/')
async def ukr_get_localities_hand():
    pass

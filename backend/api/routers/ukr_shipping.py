from fastapi import APIRouter


ukr_shipping_r = APIRouter(
    tags=['UKR'],
    prefix='/ukr'
)


@ukr_shipping_r.get('/get/localities/')
async def ukr_get_localities_hand():
    pass

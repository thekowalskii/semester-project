from fastapi import APIRouter


meest_r = APIRouter(
    tags=['MEEST'],
    prefix='/meest'
)


@meest_r.get('/get/localities/')
async def meest_get_localities_hand():
    pass

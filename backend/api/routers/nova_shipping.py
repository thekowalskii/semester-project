from fastapi import APIRouter

from backend.services.nova import HTTPClientNOVA


nova_shipping_r = APIRouter(
    tags=['NOVA'],
    prefix='/nova'
)

http_worker = HTTPClientNOVA()


@nova_shipping_r.get('/get/localities/')
async def nova_get_localities_hand():
    data = await http_worker.get_all_localities()
    return data

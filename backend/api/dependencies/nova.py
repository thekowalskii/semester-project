from typing import Annotated, Optional
import json

from fastapi import Depends, HTTPException, status

from backend.services.nova import HTTPClientNOVA
from backend.databases.redis_manager import redis_manager
from backend.utils.nova import NOVA


async def get_department_localities():
    data = await NOVA().department_localites()
    return data


async def get_courier_localities(): 
    data = await NOVA().courier_localities()
    return data


async def get_parcel_locker_localities():
    # data = await HTTPClientNOVA().get_parcel_locker_localites()
    # await check_data(data)
    # return data
    pass


department_localities = Annotated[dict, Depends(get_department_localities)]
courier_localities = Annotated[dict, Depends(get_courier_localities)]
parcel_locker_localities = Annotated[dict, Depends(get_parcel_locker_localities)]


async def localities_cache() -> Optional[str]:
    data = await redis_manager.get_cached_string_data('nova-localities')
    return data


async def localities_expired_time() -> int:
    time_to_expire = await redis_manager.ttl('nova-localities')
    return time_to_expire
    

cached_localities = Annotated[Optional[str], Depends(localities_cache)]
localities_expired = Annotated[int, Depends(localities_expired_time)]

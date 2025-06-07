import json

from fastapi import APIRouter, HTTPException, status

from backend.api.dependencies.nova import department_localities, courier_localities, parcel_locker_localities, cached_localities, localities_expired
from backend.databases.redis_manager import redis_manager
from backend.services.nova import HTTPClientNOVA
from backend.schemas.nova.nova import LocalitiesAllPublic, CachedLocalitiesPublic, LocalitiesPublic, LocalitiesDepartment, LocalitiesCourier
from backend.schemas.nova.exceptions import CacheLocalitiesAllError400, GetLocalitiesDepartmentError400, GetLocalitiesCourierError400


nova_r = APIRouter(
    tags=['NOVA'],
    prefix='/nova'
)


@nova_r.get('/get/localities/all', 
            summary="Get all localities",
            description='Returns all available localities with their info',
            response_model=LocalitiesAllPublic)
async def get_localities_all_hand(localities: cached_localities):
    response = {
        'data': None,
        'source': None
    }
    if localities:
        response["data"] = json.loads(localities)
        response["source"] = "cache"
        return response
    localities = await HTTPClientNOVA().fetch_localities()
    response["data"] = localities
    response["source"] = "api"
    return response


@nova_r.get('/get/cache/localities',
            summary="Checks cache localities data",
            description="**Checks** if there is cached localities data",
            response_model=CachedLocalitiesPublic)
async def nova_get_localities_cache_hand(localities: localities_expired):
    is_cached = localities != -2
    return {
        "isCached": is_cached,
        "expiredTime": localities if is_cached else 0
    }
    
    
@nova_r.post('/cache/localities/all',
            summary="Cache localities data",
            description="**Cache** localities data for using it in other endpoints",
            response_model=list[LocalitiesPublic],
            responses={
                400: {'model': CacheLocalitiesAllError400}
            })
async def nova_cache_localities_all_hand(localities: cached_localities):
    if localities:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Data is already cached'
            )
    data = await HTTPClientNOVA().fetch_localities()
    await redis_manager.cash_string_data('nova-localities', json.dumps(data), 3600 * 24)
    return data


@nova_r.get('/get/localities/department',
            summary="Gets department localities",
            description="Gets only localities that have **department** available",
            response_model=list[LocalitiesDepartment],
            responses={
                400: {'model': GetLocalitiesDepartmentError400}
            })
async def nova_get_localities_department_hand(localities: department_localities):
    return localities


@nova_r.get('/get/localities/courier',
            summary="Gets courier localities",
            description="Gets only localities that have **courier shipping** available",
            response_model=list[LocalitiesCourier],
            responses={
                400: {'model': GetLocalitiesCourierError400}
            })
async def nova_get_localities_courier_hand(localities: courier_localities):
    return localities


@nova_r.get('/get/localities/parcel-locker', deprecated=True)
async def nova_get_localities_parcel_locker_hand(localities: parcel_locker_localities):
    return localities

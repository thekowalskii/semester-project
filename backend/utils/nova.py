import json

from fastapi import HTTPException, status

from backend.databases.redis_manager import redis_manager


class NOVA:
    def __init__(self):
        self.template = {
            'село': 'village',
            'селище міського типу': 'urban-type settlement',
            'місто': 'city',
            'селище': 'village',
            's-село': 'v',
            's-селище міського типу': 'uts',
            's-місто': 'c',
            's-селище': 'v'
        }
    
    async def check_cached_data(self) -> str:
        data = await redis_manager.get_cached_string_data('nova-localities')
        if not data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Cached data is not found. Use /nova/cache/localities/all'
            )
        return json.loads(data)
    
    async def department_localites(self) -> list[dict]:
        localities_data = await self.check_cached_data()
        data = []
        for locality in localities_data:
            if locality["department"]:
                data.append(locality)
        return data
    
    async def courier_localities(self) -> list[dict]:
        localities_data = await self.check_cached_data()
        data = []
        for locality in localities_data:
            if locality["courier"]:
                data.append(locality)
        return data
    
    def get_template(self) -> dict:
        return self.template

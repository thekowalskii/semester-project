import uuid

import aioredis
from fastapi import HTTPException, status


class RedisManager:
    '''
    This is `Redis` database manager. Here you can see different classes those are used in this project to `initialize`,
    `connect`, `close` database and get `database session`.
    '''

    def __init__(self):
        self._engine: aioredis.Redis | None = None


    def init(self):
        self._engine = aioredis.from_url('redis://localhost')


    async def add_photo(self, title: str, photo: str) -> None:
        '''
        Adding provided photo (in str (hex)) into `Redis` database.

        Return -> `Picture id` (in Redis)
        '''

        await self._engine.set(title, photo)

        return None


    async def get_photo(self, title: str):
        photo: str = await self._engine.get(title)

        return photo
    
    async def clear_all(self):
        'CLEAR'

        await self._engine.flushdb(asynchronous=False)

redis_manager = RedisManager()

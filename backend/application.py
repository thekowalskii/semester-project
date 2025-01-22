from typing import List
from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter

from backend.databases.pg_manager import pg_manager, check_pg_connection
from backend.config import PG_CONFIG
from backend.utils.logger import app_log


class App:
    title = 'ArtStudia'
    docs_url = '/api/docs'
    redoc_url = '/api/redoc'


    @asynccontextmanager
    async def db_init_lifespan(app: FastAPI):
        pg_manager.init(PG_CONFIG) # Ініціалізуємо базу даних PostgreSQL 
        await check_pg_connection() # Перевіряємо підключення до БД
        
        yield
        await pg_manager.close()


    @classmethod
    def get_app(cls, *routes: List[APIRouter]) -> FastAPI:
        '''
        This function create and return `FastAPI` based application
        '''

        app = FastAPI(
            title=cls.title,
            docs_url=cls.docs_url,
            redoc_url=cls.redoc_url,
            lifespan=cls.db_init_lifespan
        )

        app_log.info('Started')

        if not routes:
            app_log.warning('No routers provided')

        for r in routes:
            app.include_router(r)

        return app

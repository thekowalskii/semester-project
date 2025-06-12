from typing import List
from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.cors import CORSMiddleware

from backend.databases.pg_manager import pg_manager, check_pg_connection
from backend.databases.redis_manager import redis_manager
from backend.config import PG_CONFIG, SESSION_MIDDLEWARE_SECRET_KEY
from backend.utils.logger import app_log
from backend.api.tags_metadata import tags_metadata


class App:
    title = 'ArtStudia'
    docs_url = '/api/docs'
    redoc_url = '/api/redoc'
    tags_metadata = tags_metadata

    allow_origins = [
        'http://localhost:5173',
        "http://127.0.0.1:5173"
    ]

    @asynccontextmanager
    async def db_init_lifespan(app: FastAPI):
        pg_manager.init(PG_CONFIG) # Ініціалізуємо базу даних PostgreSQL 
        await check_pg_connection() # Перевіряємо підключення до БД
        redis_manager.init()
        
        yield
        await pg_manager.close() # закриваємо БД


    @classmethod
    def get_app(cls, *routes: List[APIRouter]) -> FastAPI:
        '''
        This function create and return `FastAPI` based application
        '''

        app = FastAPI(
            title=cls.title,
            docs_url=cls.docs_url,
            redoc_url=cls.redoc_url,
            lifespan=cls.db_init_lifespan,
            openapi_tags=tags_metadata
        )

        # app.add_middleware(APIKeyMiddleware)
        app.add_middleware(SessionMiddleware, secret_key=SESSION_MIDDLEWARE_SECRET_KEY)
        app.add_middleware(
            CORSMiddleware, 
            allow_origins=cls.allow_origins,
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*']                   
        )

        app_log.info('Started')

        if not routes:
            app_log.warning('No routers provided')

        for r in routes:
            app.include_router(r)

        return app

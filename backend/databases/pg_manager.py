from typing import AsyncIterator
import contextlib

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncConnection,
    AsyncSession,
    AsyncEngine
)
from sqlalchemy import select

from backend.utils.logger import pg_log


class PGManager:
    '''
    This is PostgreSQL database manager. Here you can see different classes those are used in this project to `initialize`,
    `connect`, `close` database and get `database session`.
    '''

    def __init__(self):
        self._sessionmaker: async_sessionmaker | None = None
        self._engine: AsyncEngine | None = None


    def init(self, host: str, echo: bool = False):
        self._engine = create_async_engine(host, echo=echo)
        self._sessionmaker = async_sessionmaker(
            autocommit=False,
            expire_on_commit=False,
            bind=self._engine
        )


    async def close(self):
        if self._engine is None:
            pg_log.error("Manager Is Not initialized")

        await self._engine.dispose()

        self._engine = None
        self._sessionmaker = None


    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self._engine is None:
            pg_log.error("Manager Is Not initialized")

        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise


    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._sessionmaker is None:
            pg_log.error("Manager Is Not Initialized")

        session = self._sessionmaker()

        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


pg_manager = PGManager()


async def check_pg_connection():
    '''
    Check databse connection and log db connection status
    '''

    async with pg_manager.session() as session:
        try:
            await session.execute(select(1))
            pg_log.info('Connected')
        except Exception as _:
            pg_log.warning('Database Is Not Connected')


async def get_db_session():
    async with pg_manager.session() as session:
        yield session



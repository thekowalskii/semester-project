from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.databases.pg_manager import get_db_session


Session_dp = Annotated[AsyncSession, Depends(get_db_session)]

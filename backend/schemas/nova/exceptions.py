from pydantic import BaseModel, Field

from backend.schemas.exceptions import ErrorResponse


class CacheLocalitiesAllError400(ErrorResponse):
    detail: str = Field(examples=['Data is already cached'])


class GetLocalitiesError400Response(ErrorResponse):
    detail: str = Field(examples=['Cached data is not found. Use /nova/cache/localities/all'])


class GetLocalitiesDepartmentError400(GetLocalitiesError400Response):
    pass


class GetLocalitiesCourierError400(GetLocalitiesError400Response):
    pass

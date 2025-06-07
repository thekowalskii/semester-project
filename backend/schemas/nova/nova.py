from pydantic import BaseModel, Field

from backend.schemas.enums.nova import LocalitiesSource


class Localities(BaseModel):
    title: str = Field(examples=['Abazivka'])
    localityTypeNative: str = Field(examples=['село'])
    localityType: str = Field(examples=['village'])
    localityTypeShort: str = Field(examples=['v'])
    region: str = Field(examples=['Poltavska'])
    district: str = Field(examples=['Poltavskyi'])


class LocalitiesPublic(Localities):
    department: bool = Field(examples=[True])
    courier: bool = Field(examples=[True])
    
    
class LocalitiesDepartment(Localities):
    pass


class LocalitiesCourier(Localities):
    pass
    
    
class LocalitiesAllPublic(BaseModel):
    data: list[LocalitiesPublic]
    source: LocalitiesSource


class CachedLocalitiesPublic(BaseModel):
    isCached: bool = Field(examples=[False])
    expiredTime: int = Field(examples=[0])

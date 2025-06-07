from enum import Enum


class LocalitiesSource(str, Enum):
    CACHE = 'cache'
    API = 'api'

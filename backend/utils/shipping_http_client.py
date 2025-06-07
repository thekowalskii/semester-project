from abc import ABC, abstractmethod

from backend.utils.http_client import HTTPClient


class ShippingHTTPClient(ABC, HTTPClient):
    @abstractmethod
    async def get_department_localities():
        pass
    
    @abstractmethod
    async def get_courier_localities():
        pass
    
    @abstractmethod
    async def get_parcel_locker_localites():
        pass

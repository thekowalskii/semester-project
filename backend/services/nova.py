from typing import Union

from aiohttp import ClientSession

from backend.utils.http_client import HTTPClient
from backend.config import NOVA


class HTTPClientNOVA(HTTPClient):
    def __init__(self):
        super().__init__(
            base_url='https://api.novaposhta.ua/v2.0/json/'
        )
        
    async def get_all_localities(self) -> Union[bool, list]:
        self.endpoint = ''
        self.payload = {
              "apiKey": NOVA,
              "modelName": "Address",
              "calledMethod": "getSettlements",
              "methodProperties": {
              "Page": "1",
              "Warehouse": "1"  
  }
        }
        async with ClientSession(base_url=self.base_url) as session:
            async with session.post(url=self.endpoint, json=self.payload) as response:
                if response.status == 200:
                    data = await response.json()
                else:
                    data = False
            return data

# import asyncio
# worker = HTTPClientNOVA()

# print(asyncio.run(worker.get_all_localities()))

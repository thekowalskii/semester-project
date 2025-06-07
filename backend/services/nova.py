from typing import Union

from aiohttp import ClientSession
from fastapi import HTTPException, status

from backend.utils.shipping_http_client import ShippingHTTPClient
from backend.config import NOVA_API_KEY
from backend.utils.nova import NOVA


class HTTPClientNOVA(ShippingHTTPClient):
    def __init__(self):
        super().__init__(
            base_url='https://api.novaposhta.ua/v2.0/json/'
        )
        
    async def fetch_localities(self) -> Union[list, bool]:
        self.endpoint = ''
        self.payload = {
            "apiKey": NOVA_API_KEY,
            "modelName": "Address",
            "calledMethod": "getSettlements",
            "methodProperties": {
            "Page": "1"
            }
        }
        template = NOVA().get_template()
        data = []
        for page in range(1, 181):
            self.payload["methodProperties"]["Page"] = page
            async with self.session.post(url=self.endpoint, json=self.payload) as response:
                if response.status == 200:
                    request_data = await response.json()
                    request_data = request_data["data"][0]
                    locality_type = request_data["SettlementTypeDescription"]
                    locality_data = dict()
                    locality_data["title"] = request_data["DescriptionTranslit"]
                    locality_data['localityTypeNative'] = locality_type
                    locality_data["localityType"] = template[locality_type]
                    locality_data["localityTypeShort"] = template[f's-{locality_type}']
                    locality_data["region"] = request_data["AreaDescriptionTranslit"]
                    locality_data["district"] = request_data["RegionsDescriptionTranslit"]
                    locality_data["department"] = int(request_data["Warehouse"]) == 1
                    locality_data["courier"] = request_data["AddressDeliveryAllowed"]
                    data.append(locality_data)
                else:
                    request_data = False
                    # data.append(request_data)
        await self.close_session()
        if not data:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='NOVA api error'
            )
        return data
        
    # async def get_department_localities(self) -> Union[dict, bool]:
    #     data =  await self.fetch_localities()
    #     return data
    
    # async def get_courier_localities(self) -> Union[dict, bool]:
    #     data = await self.fetch_localities()
    #     return data
    
    # async def get_parcel_locker_localites(self) -> Union[dict, bool]:
    #     data = await self.fetch_localities()
    #     return data
    
    async def get_department_localities():
        pass
    
    async def get_courier_localities():
        pass
    
    async def get_parcel_locker_localites():
        pass


# import asyncio
# async def main():
#     async with ClientSession(base_url='https://api.novaposhta.ua/v2.0/json/') as session:
#         payload = {
#             "apiKey": NOVA_API_KEY,
#             "modelName": "Address",
#             "calledMethod": "getSettlements",
#             "methodProperties": {
#             "Page": "1"
#             }
#         }
#         async with session.post(url='', json=payload) as response:
#             data = await response.json()
#             l = 0
#             for i in data['data']:
#                 l += 1
#             print(l)
            
# asyncio.run(main())

#EXAMPLE RESPONSE
#  {
#       "Ref": "0db916d8-4b3a-11e4-ab6d-005056801329",
#       "SettlementType": "563ced13-f210-11e3-8c4a-0050568002cf",
#       "Latitude": "47.323626000000000",
#       "Longitude": "31.706945000000000",
#       "Description": "Андріївка",
#       "DescriptionRu": "Андреевка",
#       "DescriptionTranslit": "Andriivka",
#       "SettlementTypeDescription": "село",
#       "SettlementTypeDescriptionRu": "село",
#       "SettlementTypeDescriptionTranslit": "selo",
#       "Region": "e4acbd17-4b33-11e4-ab6d-005056801329",
#       "RegionsDescription": "Миколаївський",
#       "RegionsDescriptionRu": "Николаевский р-н",
#       "RegionsDescriptionTranslit": "Mykolaivskyi",
#       "Area": "dcaaddd7-4b33-11e4-ab6d-005056801329",
#       "AreaDescription": "Миколаївська",
#       "AreaDescriptionRu": "Николаевская область",
#       "AreaDescriptionTranslit": "Mykolaivska",
#       "Index1": "57104",
#       "Index2": "57104",
#       "IndexCOATSU1": "4824286010",
#       "Delivery1": "",
#       "Delivery2": "",
#       "Delivery3": "",
#       "Delivery4": "",
#       "Delivery5": "",
#       "Delivery6": "",
#       "Delivery7": "",
#       "SpecialCashCheck": 1,
#       "RadiusHomeDelivery": "500",
#       "RadiusExpressPickUp": "500",
#       "RadiusDrop": "500",
#       "Warehouse": "0",
#       "AddressDeliveryAllowed": true
#     },

from typing import Optional
# from aiohttp import ClientSession


class HTTPClient:
    def __init__(
        self, 
        base_url: str, 
        endpoint='', 
        params: Optional[dict] = None,
        payload: Optional[dict] = None
        ):
        self.base_url = base_url
        self.endpoint = endpoint
        self.params = params
        self.payload = payload
        # self.session = ClientSession(
        #     base_url=self.base_url
        # )

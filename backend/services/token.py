from time import time
import datetime

import jwt
from fastapi import HTTPException, status

from backend.config import TOKEN_ALG, TOKEN_SECRET_KEY, TOKEN_TYPE


class TokenManager:
    '''
    Hello
    '''
    def __init__(self,
                 alg: str = TOKEN_ALG,
                 type: str = TOKEN_TYPE,
                 secret_key: str = TOKEN_SECRET_KEY
    ):
        self._alg = alg
        self._type = type
        self._secret_key = secret_key


    def encode_token(self, payload):
        if not payload:
            raise ValueError('Payload cannot be empty string')

        token = jwt.encode(
            payload=payload,
            key=self._secret_key,
            algorithm=self._alg,
            headers={
                'alg': self._alg, 
                'typ': self._type,
                'exp': time() + 36000
            }
        )

        return token

    def decode_token(self, token: str):
        try:

            payload = jwt.decode(
                token,
                key=self._secret_key,
                algorithms=[self._alg],
            )

            print(f'\n\n\n{payload}\n\n\n')
        except jwt.exceptions.ExpiredSignatureError as error:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='Your access token signature has expired'
            )

        return payload

token_manager = TokenManager()

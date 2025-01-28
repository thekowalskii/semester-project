from typing import List

import passlib.context
from fastapi import HTTPException, status


class PasswordManager:
    def __init__(self,
                 scheme: str = 'bcrypt'
    ):
        self.crypto_context = passlib.context.CryptContext(schemes=[scheme])
        self._scheme = scheme

    def hash_password(self, password):
        '''
        Hash provided password
        '''

        password = self.crypto_context.hash(password)

        return password
    
    def verify_password(self, provided_password, og_password):
        is_valid = self.crypto_context.verify(provided_password, og_password, scheme=self._scheme)

        if is_valid == False:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Password is incorrect'
            )

        return is_valid


password_manager = PasswordManager()

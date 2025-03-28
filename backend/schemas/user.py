from string import ascii_letters
import uuid
from typing import Annotated

from pydantic import (BaseModel, 
                      EmailStr, 
                      Field, 
                      field_validator
)
from fastapi import Form

ascii_letters = ascii_letters + ' '


class UserSigninForm(BaseModel):
    email: EmailStr
    password: str


class UserSchema(BaseModel):
    username: str = Field(..., max_length=64)
    email: EmailStr = Field(..., max_length=128)
    password: str = Field(..., min_length=12)
    
    @field_validator('username')
    def validate_username(v):

        for letter in v:
            if letter not in ascii_letters:
                raise ValueError('Username can only contain letters (A-Z)')

        return v


class UserResponseSchema(BaseModel):
    id: uuid.UUID
    username: str
    email: EmailStr
    role: str
    cart: uuid.UUID

    model_config = {
        'from_attributes': True
    }

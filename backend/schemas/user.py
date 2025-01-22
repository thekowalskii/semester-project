from string import ascii_letters
import uuid

from pydantic import (BaseModel, 
                      EmailStr, 
                      Field, 
                      field_validator
)

ascii_letters = ascii_letters + ' '


class UserSchema(BaseModel):
    username: str 
    email: EmailStr
    password: str

    @field_validator('email')
    def validate_email(v):
        if len(v) > 128:
            raise ValueError('Email cannot be longer than 64 symbols')

        return v
    
    @field_validator('username')
    def validate_username(v):
        if len(v) > 64:
            raise ValueError('Username cannot be longer than 64 symbols')

        for letter in v:
            if letter not in ascii_letters:
                raise ValueError('Username can only contain letters (A-Z)')

        return v


class UserResponseSchema(BaseModel):
    id: uuid.UUID
    username: str
    email: EmailStr

    model_config = {
        'from_attributes': True
    }

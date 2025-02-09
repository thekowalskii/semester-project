from enum import Enum as stdEnum
import uuid

from sqlalchemy import String, Enum as saEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from fastapi import HTTPException, status

from backend.models.base import PGBase
from backend.schemas.user import UserSchema
from backend.api.dependencies.db import Session_dp
from backend.utils import password_manager

from backend.config import ADMIN_EMAIL, ADMIN_PASSWORD, ADMIN_USERNAME
from .cart import Cart


class User(PGBase):
    username: Mapped[str] = mapped_column(String(64))
    email: Mapped[str] = mapped_column(String(128), unique=True)
    password: Mapped[str] = mapped_column()
    role: Mapped[str] = mapped_column(saEnum('admin', 'user', name='user_roles'), default='user')

    cart: Mapped[uuid.UUID] = mapped_column(ForeignKey('carts.id'))

    @classmethod
    async def create(cls, session: Session_dp, user: UserSchema):
        if user.email == ADMIN_EMAIL and (user.username != ADMIN_USERNAME or user.password != ADMIN_PASSWORD):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Incorrect data'
            )
        
        cart = await Cart.create(session=session)
        
        new = cls(
            username=user.username,
            email=user.email,
            password=password_manager.hash_password(user.password),
            role='admin' if user.username == ADMIN_USERNAME and user.email == ADMIN_EMAIL and user.password == ADMIN_PASSWORD else 'user',
            cart=cart.id
        )

        session.add(new)
        await session.commit()

        return new

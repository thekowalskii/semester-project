from enum import Enum as stdEnum

from sqlalchemy import String, Enum as saEnum
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import PGBase


class User(PGBase):
    username: Mapped[str] = mapped_column(String(64))
    email: Mapped[str] = mapped_column(String(128), unique=True)
    password: Mapped[str] = mapped_column()
    role: Mapped[str] = mapped_column(saEnum('admin', 'user', name='user_roles'), default='user')

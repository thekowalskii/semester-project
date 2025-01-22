import uuid

from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs


class PGBase(AsyncAttrs, DeclarativeBase):
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'

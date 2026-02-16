from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.types.user_id import UserIdType
from .mixins.created_at import CreatedAtMixin

from .mixins.int_id_pk import IntIdPkMixin
from .base import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, IntIdPkMixin, CreatedAtMixin, SQLAlchemyBaseUserTable[UserIdType]):
    username: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)

    habits = relationship(
        "Habit",
        back_populates="user",
    )

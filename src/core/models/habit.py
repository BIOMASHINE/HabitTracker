from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base

from core.models.mixins import IntIdPkMixin, CreatedAtMixin


class Habit(Base, IntIdPkMixin, CreatedAtMixin):
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    title: Mapped[str]
    description: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)

    user = relationship(
        "User",
        back_populates="habits",
    )
    completions = relationship(
        "Completion",
        back_populates="habit",
        cascade="all, delete-orphan",
    )

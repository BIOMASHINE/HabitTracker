from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.mixins import IntIdPkMixin


class Completion(Base, IntIdPkMixin):
    habit_id: Mapped[int] = mapped_column(
        ForeignKey("habits.id"),
        nullable=False,
    )

    completed_at: Mapped[datetime] = mapped_column(server_default=func.now())

    habit = relationship(
        "Habit",
        back_populates="completions",
    )

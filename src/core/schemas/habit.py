from datetime import datetime

from pydantic import BaseModel, Field


class HabitCreate(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    description: str | None = Field(max_length=250)
    is_active: bool = Field(default=True)


class HabitUpdate(BaseModel):
    title: str | None = Field(min_length=1, max_length=50)
    description: str | None = Field(max_length=250)
    is_active: bool | None = Field(default=None)


class HabitRead(BaseModel):
    id: int
    user_id: int
    title: str
    description: str | None
    is_active: bool
    created_at: datetime

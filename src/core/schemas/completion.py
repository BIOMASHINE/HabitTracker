from datetime import datetime

from pydantic import BaseModel


class CompletionCreate(BaseModel):
    habit_id: int


class CompletionRead(BaseModel):
    id: int
    habit_id: int
    completed_at: datetime

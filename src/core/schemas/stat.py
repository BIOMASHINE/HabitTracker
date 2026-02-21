from datetime import date

from pydantic import BaseModel


class StatRead(BaseModel):
    streak: int
    max_streak: int
    total_completions: int
    dates: list[date]

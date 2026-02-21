from datetime import datetime
from typing import Annotated

from fastapi_users import schemas
from pydantic import ConfigDict, EmailStr, Field

from core.types.user_id import UserIdType

name = Annotated[
    str,
    Field(
        max_length=33,
        min_length=3,
    ),
]


class UserRead(schemas.BaseUser[UserIdType]):
    created_at: datetime
    username: name


class UserCreate(schemas.BaseUserCreate):
    username: name


class UserUpdate(schemas.BaseUserUpdate):
    username: name | None = Field(default=None)

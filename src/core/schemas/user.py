from datetime import datetime
from typing import Annotated

from fastapi_users import schemas
from pydantic import Field

from core.types.user_id import UserIdType

username = Annotated[
    str,
    Field(
        max_length=33,
        min_length=3,
    ),
]


class UserRead(schemas.BaseUser[UserIdType]):
    created_at: datetime
    username: username


class UserCreate(schemas.BaseUserCreate):
    username: username


class UserUpdate(schemas.BaseUserUpdate):
    username: username

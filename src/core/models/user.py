from fastapi_users.db import SQLAlchemyBaseUserTable

from .mixins.int_id_pk import IntIdPkMixin
from .base import Base


class User(Base, IntIdPkMixin, SQLAlchemyBaseUserTable[int]):
    pass

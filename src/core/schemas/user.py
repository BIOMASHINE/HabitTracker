from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str

class UserCreate(UserSchema):
    pass

class UserRead(UserSchema):
    id: int

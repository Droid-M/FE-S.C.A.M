from pydantic import BaseModel

class UserBase(BaseModel):
    cpf: int
    name: str
    email: str
    userType: str
    hashed_password: str
    is_active: bool

class User(UserBase):
    class Config:
        orm_mode = True
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class UserModel(Base):
    __tablename__ = "users"
    cpf = Column(String(11), unique=True, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    userType = Column(String(20))
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
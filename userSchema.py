from pydantic import BaseModel, NameEmail, validator
from datetime import datetime
#from email_validator import validate_email, EmailNotValidError     Talvez seja necessário*****
#Usar @validator pra validar os tipos datetime pois ele converte QUALQUER valor alfanumérico *********
from typing import Optional

class UserBase(BaseModel):
    createdOn: datetime
    updatedOn: Optional[datetime]
    email: NameEmail
    #hash da senha, talvez?
    
class UserCreate(BaseModel):
    email: NameEmail
    password: str
    
class UserUpdate(UserBase):
    email: NameEmail = None
    password: Optional[str] = None
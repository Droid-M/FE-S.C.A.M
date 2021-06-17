from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LogToUpload(BaseModel):
    id: int
    conteudo: str
    created_on: Optional[datetime]
    updated_on: Optional[datetime]

from pydantic import BaseModel

class Error(BaseModel):
    code: int = 500
    message: str
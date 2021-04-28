from pydantic import BaseModel


class MedicamentoBase(BaseModel):
    codigo:int
    nome: str

class MedicamentoCreate(BaseModel):
    codigo: int
    nome: str

    
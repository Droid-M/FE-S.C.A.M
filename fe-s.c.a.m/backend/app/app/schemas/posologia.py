from pydantic import BaseModel

class Posologia(BaseModel):
    id: int
    medicamento: int
    paciente: int
    dosagem: str

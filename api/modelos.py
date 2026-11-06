from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class Marcacion(BaseModel):
    empleado_id: int = Field(gt=0)
    tipo: Literal["entrada", "salida"]
    fecha_hora: datetime


class MarcacionRespuesta(BaseModel):
    marcacion_id: int
    mensaje: str
    empleado_id: int
    tipo: str
    fecha_hora: datetime
    estado: str

class EmpleadoCrear(BaseModel):
    nombre: str = Field(min_length=1, max_length=100)
    departamento: str | None = None
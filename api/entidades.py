from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from api.base_de_datos import Base


class Empleado(Base):
    __tablename__ = "empleados"

    empleado_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    departamento = Column(String(100), nullable=True)

    marcaciones = relationship("MarcacionDB", back_populates="empleado")


class MarcacionDB(Base):
    __tablename__ = "marcaciones"

    marcacion_id = Column(Integer, primary_key=True, index=True)
    empleado_id = Column(Integer, ForeignKey("empleados.empleado_id"), nullable=False)
    tipo = Column(String(10), nullable=False)
    fecha_hora = Column(DateTime, nullable=False)
    estado = Column(String(30), nullable=False)

    empleado = relationship("Empleado", back_populates="marcaciones")
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from api.modelos import Marcacion, MarcacionRespuesta, EmpleadoCrear
from api.servicios import calcular_estado
from api.base_de_datos import obtener_db
from api.entidades import Empleado, MarcacionDB

app = FastAPI()


@app.get("/")
def inicio():
    return {"mensaje": "API de marcaciones funcionando"}


@app.post("/empleados")
def crear_empleado(empleado: EmpleadoCrear, db: Session = Depends(obtener_db)):
    nuevo = Empleado(
        nombre=empleado.nombre,
        departamento=empleado.departamento
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return {
        "empleado_id": nuevo.empleado_id,
        "nombre": nuevo.nombre,
        "departamento": nuevo.departamento
    }


@app.post("/marcaciones", response_model=MarcacionRespuesta)
def recibir_marcacion(marcacion: Marcacion, db: Session = Depends(obtener_db)):

    empleado = db.query(Empleado).filter(
        Empleado.empleado_id == marcacion.empleado_id
    ).first()

    if not empleado:
        raise HTTPException(
            status_code=404,
            detail="El empleado no existe"
        )

    estado = calcular_estado(marcacion)

    nueva = MarcacionDB(
        empleado_id=marcacion.empleado_id,
        tipo=marcacion.tipo,
        fecha_hora=marcacion.fecha_hora,
        estado=estado
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return {
        "mensaje": "Marcación guardada correctamente",
        "marcacion_id": nueva.marcacion_id,
        "empleado_id": nueva.empleado_id,
        "tipo": nueva.tipo,
        "fecha_hora": nueva.fecha_hora,
        "estado": nueva.estado
    }
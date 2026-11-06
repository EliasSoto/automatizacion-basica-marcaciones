
from datetime import datetime

from api.modelos import Marcacion
from api.servicios import calcular_estado


def test_entrada_normal():
    marcacion = Marcacion(
        empleado_id=101,
        tipo="entrada",
        fecha_hora=datetime.fromisoformat("2026-11-06T08:00:00")
    )

    assert calcular_estado(marcacion) == "normal"


def test_entrada_atrasada():
    marcacion = Marcacion(
        empleado_id=101,
        tipo="entrada",
        fecha_hora=datetime.fromisoformat("2026-11-06T08:20:00")
    )

    assert calcular_estado(marcacion) == "atraso"


def test_salida_anticipada():
    marcacion = Marcacion(
        empleado_id=101,
        tipo="salida",
        fecha_hora=datetime.fromisoformat("2026-11-06T16:30:00")
    )

    assert calcular_estado(marcacion) == "salida_anticipada"


def test_salida_normal():
    marcacion = Marcacion(
        empleado_id=101,
        tipo="salida",
        fecha_hora=datetime.fromisoformat("2026-11-06T17:00:00")
    )

    assert calcular_estado(marcacion) == "normal"


def test_salida_posterior():
    marcacion = Marcacion(
        empleado_id=101,
        tipo="salida",
        fecha_hora=datetime.fromisoformat("2026-11-06T17:30:00")
    )

    assert calcular_estado(marcacion) == "salida_posterior"
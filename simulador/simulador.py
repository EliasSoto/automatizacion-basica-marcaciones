
from datetime import datetime
import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv("MAKE_WEBHOOK_URL")


def crear_marcacion(empleado_id, tipo, fecha_hora):
    return {
        "empleado_id": empleado_id,
        "tipo": tipo,
        "fecha_hora": fecha_hora
    }


def enviar_marcacion(marcacion):
    try:
        if not WEBHOOK_URL:
            raise ValueError("No se encontró la URL del webhook.")

        respuesta = requests.post(
            WEBHOOK_URL,
            json=marcacion,
            timeout=15
        )

        respuesta.raise_for_status()

        print("Marcación enviada correctamente.")
        print("Código HTTP:", respuesta.status_code)

    except ValueError as error:
        print("Error de configuración:", error)

    except requests.exceptions.RequestException as error:
        print("Error de conexión:", error)


def simular_marcaciones():

    marcaciones = [
        crear_marcacion(1, "entrada", "2026-11-06T08:00:00"),
        crear_marcacion(1, "salida", "2026-11-06T17:00:00"),

        crear_marcacion(2, "entrada", "2026-11-06T08:25:00"),
        crear_marcacion(2, "salida", "2026-11-06T17:30:00"),

        crear_marcacion(3, "entrada", "2026-11-06T08:10:00"),
        crear_marcacion(3, "salida", "2026-11-06T16:45:00"),

        crear_marcacion(4, "entrada", "2026-11-06T08:40:00"),
        crear_marcacion(4, "salida", "2026-11-06T17:15:00"),

        crear_marcacion(5, "entrada", "2026-11-06T08:15:00"),
        crear_marcacion(5, "salida", "2026-11-06T16:30:00")
    ]

    for marcacion in marcaciones:
        print("\nEnviando:", marcacion)
        enviar_marcacion(marcacion)
        time.sleep(1)


# Ejecutar simulación
simular_marcaciones()

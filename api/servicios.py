from datetime import time


def calcular_estado(marcacion):

    hora = marcacion.fecha_hora.time()

    if marcacion.tipo == "entrada":
        if hora <= time(8, 15):
            return "normal"

        return "atraso"

    if hora < time(17, 0):
        return "salida_anticipada"

    if hora == time(17, 0):
        return "normal"

    return "salida_posterior"
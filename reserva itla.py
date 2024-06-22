import json
import os


class Reserva:
    id_reserva = 1

    def __init__(self, nombre_cliente, numero_personas, fecha, hora):
        self.id = Reserva.id_reserva
        self.nombre_cliente = nombre_cliente
        self.numero_personas = numero_personas
        self.fecha = fecha
        self.hora = hora
        Reserva.id_reserva += 1

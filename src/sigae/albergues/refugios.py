class Refugio:
    """Módulo de refugios (en desarrollo)."""

    def __init__(self, nombre, distrito, capacidad):
        self.nombre = nombre
        self.distrito = distrito
        self.capacidad = capacidad
        self.ocupados = 0

    def espacios_libres(self):
        return self.capacidad - self.ocupados

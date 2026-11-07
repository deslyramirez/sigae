# Milímetros de lluvia por hora a partir de los cuales se envía la alerta.
UMBRAL_LLUVIA_MM = 50


def requiere_alerta(lluvia_mm):
    return lluvia_mm >= UMBRAL_LLUVIA_MM

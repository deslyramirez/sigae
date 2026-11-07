# Milímetros de lluvia por hora a partir de los cuales se envía la alerta.
# SCR-2026-080: se baja de 50 a 30 mm porque el Fenómeno del Niño se intensificó.
UMBRAL_LLUVIA_MM = 30


def requiere_alerta(lluvia_mm):
    return lluvia_mm >= UMBRAL_LLUVIA_MM

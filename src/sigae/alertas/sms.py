import re


def normalizar(numero):
    """Quita espacios y el código de país +51 que traen los números registrados."""
    numero = numero.replace(" ", "")
    if numero.startswith("+51"):
        numero = numero[3:]
    return numero


def numero_valido(numero):
    return re.fullmatch(r"9\d{8}", normalizar(numero)) is not None


def enviar_alertas(contactos, mensaje, pasarela):
    """Envía el mensaje a cada contacto válido y devuelve cuántos se enviaron."""
    enviados = 0
    for numero in contactos:
        if numero_valido(numero):
            pasarela.enviar(normalizar(numero), mensaje)
            enviados += 1
    return enviados

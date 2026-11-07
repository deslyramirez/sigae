import re


def numero_valido(numero):
    return re.fullmatch(r"9\d{8}", numero) is not None


def enviar_alertas(contactos, mensaje, pasarela):
    """Envía el mensaje a cada contacto válido y devuelve cuántos se enviaron."""
    enviados = 0
    for numero in contactos:
        if numero_valido(numero):
            pasarela.enviar(numero, mensaje)
            enviados += 1
    return enviados

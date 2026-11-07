from sigae.alertas.sms import numero_valido, enviar_alertas


class PasarelaPrueba:
    def __init__(self):
        self.mensajes = []

    def enviar(self, numero, texto):
        self.mensajes.append((numero, texto))


def test_numero_de_9_digitos():
    assert numero_valido("987654321")


def test_envia_alertas_a_numeros_con_codigo_de_pais():
    pasarela = PasarelaPrueba()
    contactos = ["+51987654321", "+51 912 345 678"]
    assert enviar_alertas(contactos, "Alerta: lluvia intensa", pasarela) == 2

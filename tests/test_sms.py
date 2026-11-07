from sigae.alertas.sms import numero_valido


class PasarelaPrueba:
    def __init__(self):
        self.mensajes = []

    def enviar(self, numero, texto):
        self.mensajes.append((numero, texto))


def test_numero_de_9_digitos():
    assert numero_valido("987654321")

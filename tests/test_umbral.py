from sigae.alertas.umbral import requiere_alerta


def test_alerta_desde_30_mm():
    assert requiere_alerta(30)
    assert not requiere_alerta(29)

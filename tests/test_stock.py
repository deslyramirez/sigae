from sigae.db import conectar
from sigae.albergues.stock import stock_viveres


def preparar():
    conn = conectar()
    conn.executemany(
        "INSERT INTO movimientos VALUES (?, ?, ?)",
        [("Albergue Castilla", "arroz", 100), ("Albergue Castilla", "arroz", -30),
         ("Albergue Catacaos", "agua", 500)],
    )
    return conn


def test_stock_normal():
    assert stock_viveres(preparar(), "Albergue Castilla", "arroz") == 70


def test_no_permite_inyeccion_sql():
    texto_malicioso = "x' OR '1'='1"
    assert stock_viveres(preparar(), "Albergue Castilla", texto_malicioso) == 0

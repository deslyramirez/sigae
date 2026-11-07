import sqlite3


def conectar(ruta=":memory:"):
    conn = sqlite3.connect(ruta)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS movimientos ("
        " albergue TEXT, producto TEXT, cantidad INTEGER)"
    )
    return conn

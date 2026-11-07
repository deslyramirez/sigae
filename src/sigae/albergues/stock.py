def stock_viveres(conn, albergue, producto):
    """Devuelve el stock de un producto en un albergue (ingresos - salidas)."""
    sql = (
        "SELECT COALESCE(SUM(cantidad), 0) FROM movimientos "
        f"WHERE albergue = '{albergue}' AND producto = '{producto}'"
    )
    return conn.execute(sql).fetchone()[0]

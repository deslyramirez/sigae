def stock_viveres(conn, albergue, producto):
    """Devuelve el stock de un producto en un albergue (ingresos - salidas)."""
    sql = (
        "SELECT COALESCE(SUM(cantidad), 0) FROM movimientos "
        "WHERE albergue = ? AND producto = ?"
    )
    return conn.execute(sql, (albergue, producto)).fetchone()[0]

# revisado: consulta de stock por albergue

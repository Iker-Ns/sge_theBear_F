def schema(cuenta) -> dict:
    send_cuenta = {
        "id": cuenta["id"],
        "cliente_id:": cuenta["cliente_id"],
        "precio_total": cuenta["precio_total"],
        "fecha": cuenta["fecha"],
    }
    return send_cuenta

def schemas(cuentas) -> list[dict]:
    return [schema(cuenta) for k,cuenta in cuentas.items()]
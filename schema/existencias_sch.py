def schema(existencia) -> dict:
    send_existencia = {
        "id": existencia["id"],
        "precio_unidad": existencia["precio_unidad"],
        "nombre": existencia["nombre"],
        "cantidad": existencia["cantidad"],
    }
    return send_existencia

def schemas(existencias) -> list[dict]:
    return [schema(existencia) for k,existencia in existencias.items()]
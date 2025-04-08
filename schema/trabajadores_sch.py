def schema(trabajador) -> dict:
    send_trabajador = {
        "id": trabajador["id"],
        "seguridad_social": trabajador["seguridad_social"],
        "nombre": trabajador["nombre"],
        "apellido": trabajador["apellido"],
        "cargo": trabajador["cargo"],
        "id_restaurante": trabajador["id_restaurante"],
    }
    return send_trabajador

def schemas(trabajadores) -> list[dict]:
    return [schema(trabajador) for k,trabajador in trabajadores.items()]

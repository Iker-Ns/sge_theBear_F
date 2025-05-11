def schema(cliente) -> dict:
    send_cliente = {
        "id": cliente.id,
        "nombre": cliente.nombre,
        "apellido": cliente.apellido,
        "telefono": cliente.telefono,
        "restaurante": cliente.restaurante
    }
    return send_cliente

def schemas(clientes) -> list[dict]:
    return [schema(cliente) for k,cliente in clientes.items()]

def schema(producto_cuenta) -> dict:
    send_producto_cuenta = {
        "id_cuenta": producto_cuenta["id_cuenta"],
        "id_producto": producto_cuenta["id_producto"],
    }
    return send_producto_cuenta

def schemas(productos_cuenta) -> list[dict]:
    return [schema(producto_cuenta) for k,producto_cuenta in productos_cuenta.items()]
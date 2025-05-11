def schema(producto_cuenta) -> dict:
    send_producto_cuenta = {
        "id": producto_cuenta.id,
        "cuenta_id": producto_cuenta.cuenta_id,
        "producto_id": producto_cuenta.producto_id,
        "cantidad": producto_cuenta.cantidad
    }
    return send_producto_cuenta

def schemas(productos_cuenta) -> list[dict]:
    return [schema(producto_cuenta) for producto_cuenta in productos_cuenta]

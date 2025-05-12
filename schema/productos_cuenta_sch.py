def schema(producto_cuenta) -> dict:
    send_producto_cuenta = {
        "id": producto_cuenta.id,
        "cuenta_id": producto_cuenta.cuenta_id,
        "producto_id": producto_cuenta.producto_id,
        "cantidad": producto_cuenta.cantidad,
        "cuenta" : producto_cuenta.cuenta,
        "existencia" : producto_cuenta.existencias,
    }
    return send_producto_cuenta

def producto_to_cuenta_schema(producto):
    return {
        "id": producto.id,
        "cuenta_id": producto.cuenta_id,
        "producto_id": producto.producto_id,
        "cantidad": producto.cantidad,
        "existencias": {
            "id": producto.existencias.id,
            "nombre": producto.existencias.nombre,
            "precio_unidad": producto.existencias.precio_unidad,
            "cantidad": producto.existencias.cantidad
        } if producto.existencias else None
    }


def schemas(productos_cuenta) -> list[dict]:
    return [schema(producto_cuenta) for producto_cuenta in productos_cuenta]

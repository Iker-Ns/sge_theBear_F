from datetime import datetime
from schema.productos_cuenta_sch import producto_to_cuenta_schema

def schema(cuenta):
    return {
        "id": cuenta.id,
        "cliente_id": cuenta.cliente_id,
        "precio_total": cuenta.precio_total,
        "fecha": cuenta.fecha.isoformat() if isinstance(cuenta.fecha, datetime) else cuenta.fecha,
        "cliente": cuenta.cliente,  # Si quieres serializarlo, hazlo con un cliente_schema()
        "productos": [producto_to_cuenta_schema(p) for p in cuenta.productos_to_cuenta],
    }


def schemas(cuentas):
    return [schema(cuenta) for cuenta in cuentas]

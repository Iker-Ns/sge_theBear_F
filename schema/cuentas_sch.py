from datetime import datetime

def schema(cuenta):
    return {
        "id": cuenta.id,
        "cliente_id": cuenta.cliente_id,
        "precio_total": cuenta.precio_total,
        "fecha": cuenta.fecha.isoformat() if isinstance(cuenta.fecha, datetime) else cuenta.fecha
    }

def schemas(cuentas):
    return [schema(cuenta) for cuenta in cuentas]

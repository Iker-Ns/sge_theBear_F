from datetime import datetime
from typing import List, Dict, Any

def schema(cuenta) -> Dict[str, Any]:
    return {
        "id": cuenta.id,
        "cliente_id": cuenta.cliente_id,
        "precio_total": cuenta.precio_total,
        "fecha": cuenta.fecha.isoformat() if isinstance(cuenta.fecha, datetime) else cuenta.fecha
    }

def schemas(cuentas) -> List[Dict[str, Any]]:
    return [schema(cuenta) for cuenta in cuentas]

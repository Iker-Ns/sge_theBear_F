from models.Restaurante import Restaurante

def schema(restaurante) -> dict:
    send_restaurante = {
        "id": restaurante.id,
        "nombre": restaurante.nombre,
        "direccion": restaurante.direccion,
        "codigo_postal": restaurante.codigo_postal,
    }
    return send_restaurante

def schemas(restaurantes : list[Restaurante]) -> list[dict]:
    return [schema(restaurante) for restaurante in restaurantes]

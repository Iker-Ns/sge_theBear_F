def schema(restaurante) -> dict:
    send_restaurante = {
        "id": restaurante["id"],
        "direccion": restaurante["direccion"],
        "codigo_postal": restaurante["codigo_postal"],
        "encargado": restaurante["encargado"],
    }
    return send_restaurante

def schemas(restaurantes) -> list[dict]:
    return [schema(restaurante) for k,restaurante in restaurantes.items()]

from fastapi import APIRouter
from services.restaurante import crear_restaurante, listar_restaurantes, leer_restaurante, actualizar_restaurante, borrar_restaurante

router = APIRouter()

@router.get("/restaurantes")
def obtener_restaurantes():
    """
    Obtiene una lista de restaurantes.
    """
    return {
        "Result": listar_restaurantes()
    }

@router.get("/restaurantes/{id}")
def obtener_restaurante(id: int):
    """
    Obtiene un restaurante por su ID.
    """
    return {
        "Result": leer_restaurante(id)
    }

@router.post("/restaurantes")
def crear_restaurante_endpoint(nombre: str, direccion: str, telefono: str):
    """
    Crea un nuevo restaurante.
    """
    return {
        "Result": crear_restaurante(nombre, direccion, telefono)
    }

@router.put("/restaurantes/{id}")
def actualizar_restaurante_endpoint(id: int, nombre: str, direccion: str, telefono: str):
    """
    Actualiza un restaurante existente.
    """
    return {
        "Result": actualizar_restaurante(id, nombre, direccion, telefono)
    }

@router.delete("/restaurantes/{id}")
def borrar_restaurante_endpoint(id: int):
    """
    Borra un restaurante por su ID.
    """
    return {
        "Result": borrar_restaurante(id)
    }
from fastapi import APIRouter
from fastapi.params import Depends
from sqlmodel import Session
from pydantic import BaseModel

from database.Database import Database
from services.restaurante import crear_restaurante, listar_restaurantes, leer_restaurante, actualizar_restaurante, borrar_restaurante

router = APIRouter()

class Restaurante(BaseModel):
    nombre: str
    direccion: str
    codigo_postal: int

class RestauranteEdit(BaseModel):
    id: int
    nombre: str
    direccion: str
    codigo_postal: int

@router.get("/restaurantes")
def obtener_restaurantes(database: Session = Depends(Database.get_session)):
    """
    Obtiene una lista de restaurantes.
    """
    return listar_restaurantes(database)

@router.get("/restaurantes/{id}")
def obtener_restaurante(id: int, database: Session = Depends(Database.get_session)):
    """
    Obtiene un restaurante por su ID.
    """
    return leer_restaurante(id, database)

@router.post("/restaurantes")
def crear_restaurante_endpoint(
    restaurante: Restaurante,
    database: Session = Depends(Database.get_session)
):
    """
    Crea un nuevo restaurante.
    """
    return crear_restaurante(
        restaurante.nombre,
        restaurante.direccion,
        restaurante.codigo_postal,
        database
    )

@router.put("/restaurantes/{id}")
def actualizar_restaurante_endpoint(
        restaurante: RestauranteEdit,
        database: Session = Depends(Database.get_session)
    ):
    """
    Actualiza un restaurante existente.
    """
    return actualizar_restaurante(
        restaurante.id,
        restaurante.nombre,
        restaurante.direccion,
        restaurante.codigo_postal,
        database
    )

@router.delete("/restaurantes/{id}")
def borrar_restaurante_endpoint(id: int, database: Session = Depends(Database.get_session)):
    """
    Borra un restaurante por su ID.
    """
    return borrar_restaurante(id, database)
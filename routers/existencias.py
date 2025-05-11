from fastapi import APIRouter
from fastapi.params import Depends
from sqlmodel import Session
from pydantic import BaseModel

from database.Database import Database
from services.existencia import (
    crear_existencia,
    listar_existencias,
    leer_existencia,
    actualizar_existencia,
    borrar_existencia,
)

router = APIRouter()

class Existencia(BaseModel):
    nombre: str
    precio_unidad: int
    cantidad: int

class ExistenciaEdit(BaseModel):
    id: int
    nombre: str
    precio_unidad: int
    cantidad: int

@router.get("/existencias")
def obtener_existencias(database: Session = Depends(Database.get_session)):
    """
    Obtiene una lista de existencias.
    """
    return listar_existencias(database)

@router.get("/existencias/{id}")
def obtener_existencia(id: int, database: Session = Depends(Database.get_session)):
    """
    Obtiene una existencia por su ID.
    """
    return leer_existencia(id, database)

@router.post("/existencias")
def crear_existencia_endpoint(
    existencia: Existencia,
    database: Session = Depends(Database.get_session)
):
    """
    Crea una nueva existencia.
    """
    return crear_existencia(
        existencia.nombre,
        existencia.precio_unidad,
        existencia.cantidad,
        database
    )

@router.put("/existencias/{id}")
def actualizar_existencia_endpoint(
    existencia: ExistenciaEdit,
    database: Session = Depends(Database.get_session)
):
    """
    Actualiza una existencia existente.
    """
    return actualizar_existencia(
        existencia.id,
        existencia.nombre,
        existencia.precio_unidad,
        existencia.cantidad,
        database
    )

@router.delete("/existencias/{id}")
def borrar_existencia_endpoint(id: int, database: Session = Depends(Database.get_session)):
    """
    Borra una existencia por su ID.
    """
    return borrar_existencia(id, database)

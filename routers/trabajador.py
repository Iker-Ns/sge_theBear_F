from fastapi import APIRouter
from fastapi.params import Depends
from sqlmodel import Session
from pydantic import BaseModel

from database.Database import Database
from services.trabajador import *
router = APIRouter()

class Trabajador(BaseModel):
    """
    Modelo de datos para un trabajador.
    """
    seguridad_social: str
    nombre: str
    apellido: str
    cargo: str
    id_restaurante: int

class AddTrabajador(BaseModel):
    """
    Modelo de datos para editar un trabajador.
    """
    seguridad_social: str
    nombre: str
    apellido: str
    cargo: str
    id_restaurante: int

@router.get("/trabajadores/")
async def get_trabajadores(database: Session = Depends(Database.get_session)):
    """
    Endpoint para listar todos los trabajadores.
    """
    return listar_trabajadores(database)

@router.post("/trabajadores/")
async def post_trabajador(trabajador: Trabajador, database: Session = Depends(Database.get_session)):
    """
    Endpoint para crear un nuevo trabajador.
    """
    return crear_trabajador(trabajador.seguridad_social, trabajador.nombre, trabajador.apellido, trabajador.cargo, trabajador.id_restaurante, database)

@router.get("/trabajadores/{id}")
async def get_trabajador(id: int, database: Session = Depends(Database.get_session)):
    """
    Endpoint para leer un trabajador específico por su ID.
    """
    return leer_trabajador(id, database)

@router.put("/trabajadores/{id}")
async def put_trabajador(id: int, trabajador: AddTrabajador, database: Session = Depends(Database.get_session)):
    """
    Endpoint para actualizar un trabajador existente.
    """
    return actualizar_trabajador(id, trabajador.seguridad_social, trabajador.nombre, trabajador.apellido, trabajador.cargo, trabajador.id_restaurante, database)

@router.delete("/trabajadores/{id}")
async def delete_trabajador(id: int, database: Session = Depends(Database.get_session)):
    """
    Endpoint para eliminar un trabajador específico por su ID.
    """
    return eliminar_trabajador(id, database)
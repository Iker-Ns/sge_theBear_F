from datetime import datetime

from fastapi import APIRouter
from fastapi.params import Depends
from sqlmodel import Session
from pydantic import BaseModel

from database.Database import Database
from services.cuenta import *

router = APIRouter()

class Cuenta(BaseModel):
    id_cliente : int
    precio_total: int

class CuentaEdit(BaseModel):
    id_cliente : int
    precio_total: int

@router.get("/cuenta/")
def obtener_cuentas(database: Session = Depends(Database.get_session)):
    """
    Obtiene una lista de cuentas.
    """
    return listar_cuentas(database)

@router.get("/cuenta/{id}")
def obtener_cuenta(id: int, database: Session = Depends(Database.get_session)):
    """
    Obtiene una cuenta por su ID.
    """
    return leer_cuenta(id, database)

@router.post("/cuenta/")
def crear_cuenta_endpoint(
    cuenta: Cuenta,
    database: Session = Depends(Database.get_session)
):
    """
    Crea una nueva cuenta.
    """
    return añadir_cuenta(
        cuenta.id_cliente,
        cuenta.precio_total,
        database
    )

@router.put("/cuenta/{id}")
def actualizar_cuenta_endpoint(
        id: int,
        cuenta: CuentaEdit,
        database: Session = Depends(Database.get_session)
    ):
    """
    Actualiza una cuenta existente.
    """
    return actualizar_cuenta(
        id,
        cuenta.id_cliente,
        cuenta.precio_total,
        database
    )

@router.delete("/cuenta/{id}")
def eliminar_cuenta(id: int, database: Session = Depends(Database.get_session)):
    """
    Elimina una cuenta por su ID.
    """
    return borrar_cuenta(id, database)

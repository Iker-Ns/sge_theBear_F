from fastapi import APIRouter
from fastapi.params import Depends
from pydantic import BaseModel

from database.Database import Database
from services.producto_cuenta import *

router = APIRouter()

class ProductoCuenta(BaseModel):
    cuenta_id: int
    producto_id: int
    cantidad: int

class ProductoCuentaEdit(BaseModel):
    id: int
    cuenta_id: int
    producto_id: int
    cantidad: int

@router.get("/producto_cuenta/")
def obtener_productos_cuenta(database: Session = Depends(Database.get_session)):
    """
    Obtiene una lista de todas las relaciones producto-cuenta.
    """
    return listar_productos_cuenta(database)

@router.get("/producto_cuenta/{id}")
def obtener_producto_cuenta(id: int, database: Session = Depends(Database.get_session)):
    """
    Obtiene una relación producto-cuenta por su ID.
    """
    return leer_producto_cuenta(id, database)

@router.get("/producto_cuenta/cuenta/{cuenta_id}")
def obtener_productos_por_cuenta(cuenta_id: int, database: Session = Depends(Database.get_session)):
    """
    Obtiene todas las relaciones producto-cuenta asociadas a una cuenta específica.
    """
    return listar_productos_cuenta_por_cuenta(cuenta_id, database)

@router.post("/producto_cuenta/")
def crear_producto_cuenta(
    producto_cuenta: ProductoCuenta,
    database: Session = Depends(Database.get_session)
):
    """
    Crea una nueva relación producto-cuenta.
    """
    return añadir_producto_cuenta(
        producto_cuenta.cuenta_id,
        producto_cuenta.producto_id,
        producto_cuenta.cantidad,
        database
    )

@router.put("/producto_cuenta/")
def actualizar_producto_cuenta_endpoint(
    producto_cuenta: ProductoCuentaEdit,
    database: Session = Depends(Database.get_session)
):
    """
    Actualiza una relación producto-cuenta existente.
    """
    return actualizar_producto_cuenta(
        producto_cuenta.id,
        producto_cuenta.cuenta_id,
        producto_cuenta.producto_id,
        producto_cuenta.cantidad,
        database
    )

@router.delete("/producto_cuenta/{id}")
def eliminar_producto_cuenta(id: int, database: Session = Depends(Database.get_session)):
    """
    Elimina una relación producto-cuenta por su ID.
    """
    return borrar_producto_cuenta(id, database)

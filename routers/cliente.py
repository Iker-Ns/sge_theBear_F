from fastapi import APIRouter
from fastapi.params import Depends
from sqlmodel import Session
from pydantic import BaseModel

from database.Database import Database
from services.restaurante import crear_restaurante, listar_restaurantes, leer_restaurante, actualizar_restaurante, borrar_restaurante
from services.cliente import crear_cliente, listar_clientes, leer_cliente, actualizar_cliente, eliminar_cliente

router = APIRouter()

class Cliente(BaseModel):
    nombre: str
    apellido: str
    telefono: str
    restaurante_id: int
    
class ClienteEdit(BaseModel):
    id: int
    nombre: str
    apellido: str
    telefono: str
    restaurante_id: int


@router.get("/clientes")
def obtener_clientes(database: Session = Depends(Database.get_session)):
    """
    Obtiene una lista de clientes.
    """
    return listar_clientes(database)

@router.get("/clientes/{id}")
def obtener_cliente(id: int, database: Session = Depends(Database.get_session)):
    """
    Obtiene un cliente por su ID.
    """
    return leer_cliente(id, database)

@router.post("/clientes")
def crear_cliente_endpoint(
    cliente: Cliente,
    database: Session = Depends(Database.get_session)
):
    """
    Crea un nuevo cliente.
    """
    return crear_cliente(
        cliente.nombre,
        cliente.apellido,
        cliente.telefono,
        cliente.restaurante_id,
        database
    )

@router.put("/clientes/{id}")
def actualizar_cliente_endpoint(
    cliente: ClienteEdit,
    database: Session = Depends(Database.get_session)
):
    """
    Actualiza un cliente existente.
    """
    return actualizar_cliente(
        cliente.id,
        cliente.nombre,
        cliente.apellido,
        cliente.telefono,
        cliente.restaurante_id,
        database
    )

@router.delete("/clientes/{id}")
def eliminar_cliente_endpoint(id: int, database: Session = Depends(Database.get_session)):
    """
    Elimina un cliente por su ID.
    """
    return eliminar_cliente(id, database)


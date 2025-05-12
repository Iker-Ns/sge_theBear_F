from sqlmodel import Session, select
from schema.existencias_sch import schema, schemas
from models.Existencias import Existencias

def crear_existencia(nombre, precio_unidad, cantidad, database: Session):
    """
    Crea una nueva existencia con los datos proporcionados.
    """
    nueva_existencia = Existencias(nombre=nombre, precio_unidad=precio_unidad, cantidad=cantidad)
    database.add(nueva_existencia)
    database.commit()
    database.refresh(nueva_existencia)
    return {
        "Result": schema(nueva_existencia)
    }

def listar_existencias(database: Session):
    """
    Lista todas las existencias en la base de datos.
    """
    statement = select(Existencias)
    existencias = database.exec(statement).all()
    return {
        "Result": schemas(existencias)
    }

def leer_existencia(id: int, database: Session):
    """
    Lee una existencia por su ID.
    """
    statement = select(Existencias).where(Existencias.id == id)
    existencia = database.exec(statement).first()
    if existencia:
        return {
            "Result": schema(existencia)
        }
    else:
        return {
            "Error": "Existencia no encontrada"
        }

def actualizar_existencia(id: int, nombre: str, precio_unidad: int, cantidad: int, database: Session):
    """
    Actualiza una existencia existente con nuevos datos.
    """
    statement = select(Existencias).where(Existencias.id == id)
    existencia = database.exec(statement).first()
    if existencia:
        existencia.nombre = nombre
        existencia.precio_unidad = precio_unidad
        existencia.cantidad = cantidad
        database.commit()
        database.refresh(existencia)
        return {
            "Result": schema(existencia)
        }
    else:
        return {
            "Error": "Existencia no encontrada"
        }

def borrar_existencia(id: int, database: Session):
    """
    Elimina una existencia por su ID.
    """
    statement = select(Existencias).where(Existencias.id == id)
    existencia = database.exec(statement).first()
    if existencia:
        database.delete(existencia)
        database.commit()
        return {
            "Result": "Existencia eliminada"
        }
    else:
        return {
            "Error": "Existencia no encontrada"
        }
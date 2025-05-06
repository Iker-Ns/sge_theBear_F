from sqlmodel import Session, select
from schema.restaurantes_sch import schema, schemas
from models.Restaurante import Restaurante

def crear_restaurante(nombre, direccion, telefono, database : Session):
    """
    Crea un nuevo restaurante con los datos proporcionados.
    """
    restaurante_nuevo = Restaurante(nombre=nombre, direccion=direccion, telefono=telefono)
    database.add(restaurante_nuevo)
    database.commit()
    database.refresh(restaurante_nuevo)
    return { 
        "Result" : schema(restaurante_nuevo)
    }

def listar_restaurantes(database : Session):
    """
    Lista todos los restaurantes en la base de datos.
    """
    statement = select(Restaurante)
    restaurantes = database.exec(statement).all()
    return { 
        "Result" : schemas(restaurantes)
    }

def leer_restaurante(id, database : Session):
    """
    Lee un restaurante por su ID.
    """
    statement = select(Restaurante).where(Restaurante.id == id)
    restaurante = database.exec(statement).first()
    if restaurante:
        return { 
            "Result" : schema(restaurante)
        }
    else:
        return { 
            "Error" : "Restaurante no encontrado"
        }

def actualizar_restaurante(id, nombre, direccion, telefono, database : Session):
    """
    Actualiza un restaurante existente con los nuevos datos proporcionados.
    """
    statement = select(Restaurante).where(Restaurante.id == id)
    restaurante = database.exec(statement).first()
    if restaurante:
        restaurante.nombre = nombre
        restaurante.direccion = direccion
        restaurante.telefono = telefono
        database.commit()
        database.refresh(restaurante)
        return { 
            "Result" : schema(restaurante)
        }
    else:
        return { 
            "Error" : "Restaurante no encontrado"
        }
    
def borrar_restaurante(id, database : Session):
    """
    Elimina un restaurante por su ID.
    """
    statement = select(Restaurante).where(Restaurante.id == id)
    restaurante = database.exec(statement).first()
    if restaurante:
        database.delete(restaurante)
        database.commit()
        return { 
            "Result" : "Restaurante eliminado"
        }
    else:
        return { 
            "Error" : "Restaurante no encontrado"
        }
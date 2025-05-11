from sqlmodel import Session, select
from schema.restaurantes_sch import schema, schemas
from models.Restaurante import Restaurante

def crear_restaurante(nombre, direccion, codigo_postal, database : Session):
    restaurante_nuevo = Restaurante(nombre=nombre, direccion=direccion, codigo_postal=codigo_postal)
    database.add(restaurante_nuevo)
    database.commit()
    database.refresh(restaurante_nuevo)
    return { 
        "Result" : schema(restaurante_nuevo)
    }

def listar_restaurantes(database : Session):
    statement = select(Restaurante)
    restaurantes = database.exec(statement).all()
    return {
        "Result" : schemas(restaurantes)
    }

def leer_restaurante(id : int, database : Session):
    statement = select(Restaurante).where(Restaurante.id == id)
    restaurante = database.exec(statement).first()
    if restaurante:
        return { 
            "Result" : schema(restaurante)
        }
    return None

def actualizar_restaurante(id, nombre, direccion, codigo_postal, database : Session):
    statement = select(Restaurante).where(Restaurante.id == id)
    restaurante = database.exec(statement).first()
    if restaurante:
        restaurante.nombre = nombre
        restaurante.direccion = direccion
        restaurante.codigo_postal = codigo_postal
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
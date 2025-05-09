from sqlmodel import Session, select
from schema.trabajadores_sch import schema
from models.Trabajador import Trabajador

def crear_trabajador(id, seguridad_social, nombre, apellido, cargo, id_restaurante, database : Session):
    """
    Crea un nuevo trabajador con los datos proporcionados.
    """
    trabajador_nuevo = Trabajador(id=id, seguridad_social=seguridad_social, nombre=nombre, apellido=apellido, cargo=cargo, id_restaurante=id_restaurante)
    database.add(trabajador_nuevo)
    database.commit()
    database.refresh(trabajador_nuevo)
    return { 
        "Result" : schema(trabajador_nuevo)
    }

def listar_trabajadores(database : Session):
    """
    Lista todos los trabajadores en la base de datos.
    """
    trabajadores = database.exec(select(Trabajador)).all()
    return {
        "Result" : [schema(trabajador) for trabajador in trabajadores]
    }

def leer_trabajador(id, database : Session):
    """
    Lee un trabajador específico por su ID.
    """
    trabajador = database.exec(select(Trabajador).where(Trabajador.id == id)).first()
    if trabajador:
        return {
            "Result" : schema(trabajador)
        }
    else:
        return {
            "Error" : "Trabajador no encontrado"
        }

def actualizar_trabajador(id, seguridad_social, nombre, apellido, cargo, id_restaurante, database : Session):
    """
    Actualiza un trabajador existente con los nuevos datos proporcionados.
    """
    trabajador = database.exec(select(Trabajador).where(Trabajador.id == id)).first()
    if trabajador:
        trabajador.seguridad_social = seguridad_social
        trabajador.nombre = nombre
        trabajador.apellido = apellido
        trabajador.cargo = cargo
        trabajador.id_restaurante = id_restaurante
        database.commit()
        database.refresh(trabajador)
        return {
            "Result" : schema(trabajador)
        }
    else:
        return {
            "Error" : "Trabajador no encontrado"
        }
        
def eliminar_trabajador(id, database : Session):    
    """
    Elimina un trabajador específico por su ID.
    """
    trabajador = database.exec(select(Trabajador).where(Trabajador.id == id)).first()
    if trabajador:
        database.delete(trabajador)
        database.commit()
        return {
            "Result" : "Trabajador eliminado"
        }
    else:
        return {
            "Error" : "Trabajador no encontrado"
        }
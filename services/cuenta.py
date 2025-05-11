from sqlmodel import Session, select
from schema.cuentas_sch import schema, schemas
from models.Cuenta import Cuenta

def borrar_cuenta(id, database : Session):
    """
    Borra una cuenta por su ID.
    """
    statement = select(Cuenta).where(Cuenta.id == id)
    cuenta = database.exec(statement).first()
    if cuenta:
        database.delete(cuenta)
        database.commit()
        return {
            "Result" : "Cuenta borrada"
        }
    else:
        return {
            "Error" : "Cuenta no encontrada"
        }

def añadir_cuenta(cliente_id, precio_total, database : Session):
    """
    Crea una nueva cuenta con los datos proporcionados.
    """
    cuenta_nueva = Cuenta(cliente_id=cliente_id, precio_total=precio_total)
    database.add(cuenta_nueva)
    database.commit()
    database.refresh(cuenta_nueva)
    return {
        "Result" : schema(cuenta_nueva)
    }

def listar_cuentas(database : Session):
    """
    Lista todas las cuentas en la base de datos.
    """
    statement = select(Cuenta)
    cuentas = database.exec(statement).all()
    return {
        "Result" : schemas(cuentas)
    }

def leer_cuenta(id : int, database : Session):
    """
    Lee una cuenta por su ID.
    """
    statement = select(Cuenta).where(Cuenta.id == id)
    cuenta = database.exec(statement).first()
    if cuenta:
        return {
            "Result" : schema(cuenta)
        }
    return None

def actualizar_cuenta(id, cliente_id, precio_total, database : Session):
    """
    Actualiza una cuenta existente con los nuevos datos proporcionados.
    """
    statement = select(Cuenta).where(Cuenta.id == id)
    cuenta = database.exec(statement).first()
    if cuenta:
        cuenta.cliente_id = cliente_id
        cuenta.precio_total = precio_total
        database.commit()
        database.refresh(cuenta)
        return {
            "Result" : schema(cuenta)
        }
    else:
        return {
            "Error" : "Cuenta no encontrada"
        }

from sqlmodel import Session, select
from schema.cuentas_sch import schema as cuenta_schema, schemas as cuentas_schemas
from models.Cuenta import Cuenta
from services.producto_cuenta import *
from models.ProductosToCuenta import Productos_To_Cuenta


def borrar_cuenta(id, database: Session):
    """
    Borra una cuenta por su ID.
    """
    # Primero borramos los productos asociados a la cuenta
    statement = select(Productos_To_Cuenta).where(Productos_To_Cuenta.cuenta_id == id)
    productos_cuenta = database.exec(statement).all()
    for producto_cuenta in productos_cuenta:
        database.delete(producto_cuenta)

    statement = select(Cuenta).where(Cuenta.id == id)
    cuenta = database.exec(statement).first()
    if cuenta:
        database.delete(cuenta)
        database.commit()
        return {
            "Result": "Cuenta borrada"
        }
    else:
        return {
            "Error": "Cuenta no encontrada"
        }


def añadir_cuenta(cliente_id, precio_total, database: Session):
    cuenta_nueva = Cuenta(cliente_id=cliente_id, precio_total=precio_total)
    database.add(cuenta_nueva)
    database.commit()
    database.refresh(cuenta_nueva)
    return {
        "Result": cuenta_schema(cuenta_nueva)
    }


def listar_cuentas(database: Session):
    statement = select(Cuenta)
    cuentas = database.exec(statement).all()
    return {
        "Result": cuentas_schemas(cuentas)
    }


def leer_cuenta(id: int, database: Session):
    statement = select(Cuenta).where(Cuenta.id == id)
    cuenta = database.exec(statement).first()
    if cuenta:
        cuenta_data = cuenta_schema(cuenta)
        # Obtener los productos asociados a la cuenta
        productos = listar_productos_cuenta_por_cuenta(id, database)
        cuenta_data["productos"] = productos.get("Result", [])
        return {
            "Result": cuenta_data
        }
    return None


def actualizar_cuenta(id, cliente_id, precio_total, database: Session):
    statement = select(Cuenta).where(Cuenta.id == id)
    cuenta = database.exec(statement).first()
    if cuenta:
        cuenta.cliente_id = cliente_id
        cuenta.precio_total = precio_total
        database.commit()
        database.refresh(cuenta)
        return {
            "Result": cuenta_schema(cuenta)
        }
    else:
        return {
            "Error": "Cuenta no encontrada"
        }


def añadir_producto_a_cuenta(cuenta_id, producto_id, cantidad, database: Session):
    return añadir_producto_cuenta(cuenta_id, producto_id, cantidad, database)


def borrar_producto_de_cuenta(id, database: Session):
    return borrar_producto_cuenta(id, database)


def actualizar_producto_en_cuenta(id, cuenta_id, producto_id, cantidad, database: Session):
    return actualizar_producto_cuenta(id, cuenta_id, producto_id, cantidad, database)


def obtener_productos_de_cuenta(cuenta_id, database: Session):
    return listar_productos_cuenta_por_cuenta(cuenta_id, database)

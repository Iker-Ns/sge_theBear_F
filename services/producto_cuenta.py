from sqlmodel import Session, select
from schema.productos_cuenta_sch import schema, schemas
from models.ProductosToCuenta import Productos_To_Cuenta

def borrar_producto_cuenta(id, database: Session):
    statement = select(Productos_To_Cuenta).where(Productos_To_Cuenta.id == id)
    producto_cuenta = database.exec(statement).first()
    if producto_cuenta:
        database.delete(producto_cuenta)
        database.commit()
        return {
            "Result": "Producto borrado"
        }
    else:
        return {
            "Error": "Producto no encontrado"
        }

def añadir_producto_cuenta(cuenta_id, producto_id, cantidad, database: Session):
    producto_cuenta_nuevo = Productos_To_Cuenta(cuenta_id=cuenta_id, producto_id=producto_id, cantidad=cantidad)
    database.add(producto_cuenta_nuevo)
    database.commit()
    database.refresh(producto_cuenta_nuevo)
    return {
        "Result": schema(producto_cuenta_nuevo)
    }

def listar_productos_cuenta(database: Session):
    statement = select(Productos_To_Cuenta)
    productos_cuenta = database.exec(statement).all()
    return {
        "Result": schemas(productos_cuenta)
    }

def leer_producto_cuenta(id: int, database: Session):
    statement = select(Productos_To_Cuenta).where(Productos_To_Cuenta.id == id)
    producto_cuenta = database.exec(statement).first()
    if producto_cuenta:
        return {
            "Result": schema(producto_cuenta)
        }
    return None

def actualizar_producto_cuenta(id, cuenta_id, producto_id, cantidad, database: Session):
    statement = select(Productos_To_Cuenta).where(Productos_To_Cuenta.id == id)
    producto_cuenta = database.exec(statement).first()
    if producto_cuenta:
        producto_cuenta.cuenta_id = cuenta_id
        producto_cuenta.producto_id = producto_id
        producto_cuenta.cantidad = cantidad
        database.commit()
        database.refresh(producto_cuenta)
        return {
            "Result": schema(producto_cuenta)
        }
    else:
        return {
            "Error": "Producto no encontrado"
        }

def listar_productos_cuenta_por_cuenta(cuenta_id, database: Session):
    statement = select(Productos_To_Cuenta).where(Productos_To_Cuenta.cuenta_id == cuenta_id)
    productos_cuenta = database.exec(statement).all()
    return {
        "Result": schemas(productos_cuenta)
    }
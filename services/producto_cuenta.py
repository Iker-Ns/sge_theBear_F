from sqlmodel import Session, select
from schema.productos_cuenta_sch import schema, schemas
from models.ProductosToCuenta import Productos_To_Cuenta
from models.Existencias import Existencias
from fastapi import HTTPException

def borrar_producto_cuenta(id, database: Session):
    statement = select(Productos_To_Cuenta).where(Productos_To_Cuenta.id == id)
    producto_cuenta = database.exec(statement).first()

    if not producto_cuenta:
        return {
            "Error": "Producto no encontrado"
        }

    existencias = database.get(Existencias, producto_cuenta.producto_id)
    if not existencias:
        raise HTTPException(status_code=404, detail="Existencias no encontradas")

    existencias.cantidad += producto_cuenta.cantidad
    database.delete(producto_cuenta)
    database.commit()
    
    return {
        "Result": "Producto borrado"
    }


def añadir_producto_cuenta(cuenta_id, producto_id, cantidad, database: Session):
    producto = database.get(Existencias, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    if producto.cantidad < cantidad:
        raise HTTPException(status_code=400, detail="No hay suficiente cantidad disponible")

    producto_cuenta_nuevo = Productos_To_Cuenta(
        cuenta_id=cuenta_id,
        producto_id=producto_id,
        cantidad=cantidad
    )
    producto.cantidad -= cantidad
    database.add(producto_cuenta_nuevo)
    database.commit()

    database.refresh(producto)
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
    if not producto_cuenta:
        return {"Error": "Producto en cuenta no encontrado"}

    if cantidad < 0:
        raise HTTPException(status_code=400, detail="La cantidad no puede ser negativa")

    producto_actual = database.get(Existencias, producto_cuenta.producto_id)
    producto_nuevo = database.get(Existencias, producto_id)
    if not producto_nuevo:
        raise HTTPException(status_code=404, detail="Producto destino no encontrado")

    if producto_cuenta.producto_id != producto_id:
        producto_actual.cantidad += producto_cuenta.cantidad
        if producto_nuevo.cantidad < cantidad:
            raise HTTPException(status_code=400, detail="No hay suficiente cantidad disponible en el nuevo producto")
        producto_nuevo.cantidad -= cantidad
        producto_cuenta.producto_id = producto_id
    else:
        diferencia = cantidad - producto_cuenta.cantidad
        if diferencia > 0:
            if producto_actual.cantidad < diferencia:
                raise HTTPException(status_code=400, detail="No hay suficiente cantidad disponible")
            producto_actual.cantidad -= diferencia
        else:
            producto_actual.cantidad += abs(diferencia)

    producto_cuenta.cuenta_id = cuenta_id
    producto_cuenta.cantidad = cantidad

    database.commit()
    database.refresh(producto_cuenta)

    return {"Result": schema(producto_cuenta)}

def listar_productos_cuenta_por_cuenta(cuenta_id, database: Session):
    statement = select(Productos_To_Cuenta).where(Productos_To_Cuenta.cuenta_id == cuenta_id)
    productos_cuenta = database.exec(statement).all()
    return {
        "Result": schemas(productos_cuenta)
    }
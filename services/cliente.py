from sqlmodel import Session, select
from schema.clientes_sch import schema
from models.Cliente import Cliente

def crear_cliente(nombre, apellido, telefono, restaurante_id, database : Session):
    """
    Crea un nuevo cliente con los datos proporcionados.
    """
    cliente_nuevo = Cliente(nombre=nombre, apellido=apellido, telefono=telefono, restaurante_id=restaurante_id)
    database.add(cliente_nuevo)
    database.commit()
    database.refresh(cliente_nuevo)
    return { 
        "Result" : schema(cliente_nuevo)
    }
    
def listar_clientes(database : Session):
    """
    Lista todos los clientes en la base de datos.
    """
    clientes = database.exec(select(Cliente)).all()
    return {
        "Result" : [schema(cliente) for cliente in clientes]
    }


def listar_clientes_restaurante(id_restaurante, database : Session):
    """
    Lista todos los clientes de un restaurante específico.
    """
    clientes = database.exec(select(Cliente).where(Cliente.restaurante_id == id_restaurante)).all()
    return {
        "Result" : [schema(cliente) for cliente in clientes]
    }

def leer_cliente(id, database : Session):
    """
    Lee un cliente específico por su ID.
    """
    cliente = database.exec(select(Cliente).where(Cliente.id == id)).first()
    if cliente:
        return {
            "Result" : schema(cliente)
        }
    else:
        return {
            "Error" : "Cliente no encontrado"
        }
        
def actualizar_cliente(id, nombre, apellido, telefono, restaurante_id, database : Session):
    """
    Actualiza un cliente existente con los nuevos datos proporcionados.
    """
    cliente = database.exec(select(Cliente).where(Cliente.id == id)).first()
    if cliente:
        cliente.nombre = nombre
        cliente.apellido = apellido
        cliente.telefono = telefono
        cliente.restaurante_id = restaurante_id
        database.commit()
        database.refresh(cliente)
        return {
            "Result" : schema(cliente)
        }
    else:
        return {
            "Error" : "Cliente no encontrado"
        }         
        
def eliminar_cliente(id, database : Session):    
    """
    Elimina un cliente específico por su ID.
    """
    cliente = database.exec(select(Cliente).where(Cliente.id == id)).first()
    if cliente:
        database.delete(cliente)
        database.commit()
        return {
            "Result" : "Cliente eliminado"
        }
    else:
        return {
            "Error" : "Cliente no encontrado"
        }

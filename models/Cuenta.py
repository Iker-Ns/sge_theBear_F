from datetime import datetime
from sqlmodel import SQLModel, Field

class Cuenta(SQLModel, table=True):
    """
    Esta clase representa una cuenta asociada a un cliente. Cada instancia de Cuenta almacena la información
    relacionada con una transacción o conjunto de transacciones, incluyendo su identificador único, el identificador
    del cliente al que pertenece, el precio total asociado y la fecha de creación de la cuenta.

    Atributos:
        id (int): Identificador único de la cuenta. Es la clave primaria.
        cliente_id (int): Identificador del cliente asociado. Es una clave foránea que hace referencia a la entidad Cliente.
        precio_total (int): Representa el precio total o monto asociado a la cuenta.
        fecha (datetime): Fecha y hora de creación de la cuenta. Se establece por defecto con la fecha y hora actual.
    """
    id: int = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="cliente.id", nullable=False) # Cuenta N .. 1 Cliente
    precio_total: int = Field(nullable=False)
    fecha: datetime = Field(default_factory=lambda: datetime.now())
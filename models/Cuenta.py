from datetime import datetime
from sqlmodel import SQLModel, Field

class Cuenta(SQLModel, table=True):
    """
    Representa una cuenta asociada a un cliente.

    Atributos
    ---------
    id : int
        Identificador único de la cuenta (PK, Auto_Increment).
    cliente_id : int
        Identificador del cliente asociado (FK).
    precio_total : int
        Precio total asociado a la cuenta.
    fecha : datetime
        Fecha y hora de creación de la cuenta. Se establece por defecto con la fecha y hora actual.
    """
    id: int = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="cliente.id", nullable=False) # Cuenta N .. 1 Cliente
    precio_total: int = Field(nullable=False)
    fecha: datetime = Field(default_factory=lambda: datetime.now())
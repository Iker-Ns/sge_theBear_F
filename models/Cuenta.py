from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from models.Cliente import Cliente
from models.ProductosToCuenta import Productos_To_Cuenta
from typing import List

class Cuenta(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="cliente.id", nullable=False)
    precio_total: int = Field(nullable=False)
    fecha: datetime = Field(default_factory=lambda: datetime.utcnow())

    cliente: "Cliente" = Relationship(back_populates="cuentas")
    productos_to_cuenta: List["Productos_To_Cuenta"] = Relationship(back_populates="cuenta")
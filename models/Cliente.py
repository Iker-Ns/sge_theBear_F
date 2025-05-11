from sqlmodel import SQLModel, Field, Relationship
from models.Restaurante import Restaurante
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.Cuenta import Cuenta

class Cliente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=50, nullable=False)
    apellido: str = Field(max_length=50, nullable=False)
    telefono: str = Field(max_length=15, nullable=False)
    restaurante_id: int = Field(foreign_key="restaurante.id", nullable=False)

    restaurante: "Restaurante" = Relationship()
    cuentas: List["Cuenta"] = Relationship(back_populates="cliente")

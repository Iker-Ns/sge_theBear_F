from sqlmodel import SQLModel, Field, Relationship
from models.Restaurante import Restaurante
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.Cuenta import Cuenta

class Cliente(SQLModel, table=True):
    """
    Representa un Cliente.

    Atributos:
    ---------
    id : int
        Identificador único del cliente (PK, Auto_Increment).
    nombre : str
        Nombre del cliente. Longitud máxima de 50 caracteres.
    apellido : str
        Apellido del cliente. Longitud máxima de 50 caracteres.
    telefono : str
        Número de teléfono del cliente. Longitud máxima de 15 caracteres.
    restaurante : Restaurante
        FK que referencia al Restaurante asociado.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=50, nullable=False)
    apellido: str = Field(max_length=50, nullable=False)
    telefono: str = Field(max_length=15, nullable=False)
    restaurante_id: int = Field(foreign_key="restaurante.id", nullable=False)

    restaurante: "Restaurante" = Relationship()
    cuentas: List["Cuenta"] = Relationship(back_populates="cliente")

from sqlmodel import SQLModel, Field
from Restaurante import Restaurante

class Cliente(SQLModel, table=True):
    """
    Representa un Cliente.

    Atributos:
    ---------
    id : int
        Identificador único del cliente (PK, Auto_Increment).
    nombre : str
        Nombre del cliente. Campo obligatorio con una longitud máxima de 50 caracteres.
    apellido : str
        Apellido del cliente. Campo obligatorio con una longitud máxima de 50 caracteres.
    telefono : str
        Número de teléfono del cliente. Campo obligatorio con una longitud máxima de 15 caracteres.
    restaurante : Restaurante
        FK que referencia al Restaurante asociado. Campo obligatorio..
    """
    id: int = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=50, nullable=False)
    apellido: str = Field(max_length=50, nullable=False)
    telefono: str = Field(max_length=15, nullable=False)
    restaurante: Restaurante = Field(foreign_key="restaurante.id", nullable=False) # Cliente N .. 1 Restaurante
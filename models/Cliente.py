from sqlmodel import SQLModel, Field
from Restaurante import Restaurante

class Cliente(SQLModel, table=True):
    """
    Representa un Cliente.

    Atributos:
        id (int): Identificador único del cliente. Es la clave primaria.
        nombre (str): Nombre del cliente. Es obligatorio y su longitud máxima es de 50 caracteres.
        apellido (str): Apellido del cliente. Es obligatorio y su longitud máxima es de 50 caracteres.
        telefono (str): Número de teléfono del cliente. Es obligatorio y su longitud máxima es de 15 caracteres.
        restaurante (Restaurante): Objeto Restaurante asociado, indicando a cuál restaurante pertenece el cliente. Es obligatorio y se establece mediante clave externa.
    """
    id: int = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=50, nullable=False)
    apellido: str = Field(max_length=50, nullable=False)
    telefono: str = Field(max_length=15, nullable=False)
    restaurante: Restaurante = Field(foreign_key="restaurante.id", nullable=False) # Cliente N .. 1 Restaurante
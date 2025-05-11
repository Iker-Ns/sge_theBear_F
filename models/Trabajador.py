from sqlmodel import SQLModel, Field, Relationship
from models.Restaurante import Restaurante

class Trabajador(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    seguridad_social: int = Field(nullable=False)
    nombre: str = Field(max_length=50, nullable=False)
    apellido: str = Field(max_length=50, nullable=False)
    cargo: str = Field(max_length=50, nullable=False)
    id_restaurante: int = Field(foreign_key="restaurante.id", nullable=False) # Trabajadores N .. 1 Restaurante
    restaurante : Restaurante = Relationship()
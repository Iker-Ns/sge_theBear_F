from sqlmodel import SQLModel, Field

class Restaurante(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=50, nullable=False)
    direccion: str = Field(max_length=100, nullable=False)
    codigo_postal: str = Field(nullable=False)
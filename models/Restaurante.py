from sqlmodel import SQLModel, Field

class Restaurante(SQLModel, table=True):
    """"
    Representa un restaurante.
    
    Atributos
    ---------
    id : int
        Identificador único del restaurante (PK, Auto_Increment).
    nombre : str
        Nombre del restaurante (máximo 50 caracteres).
    direccion : str
        Dirección del restaurante (máximo 100 caracteres).
    codigo_postal : int
        Código postal del restaurante.
    """
    id: int = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=50, nullable=False)
    direccion: str = Field(max_length=100, nullable=False)
    codigo_postal: str = Field(nullable=False)
from sqlmodel import SQLModel, Field

class Restaurante(SQLModel, table=True):
    """"
    Representa un restaurante.
    
    Atributos
    ---------
    id : int
        Identificador único del restaurante (PK, Auto_Increment).
    direccion : str
        Dirección del restaurante (máximo 100 caracteres).
    codigo_postal : int
        Código postal del restaurante.
    encargado : Trabajador
        Trabajador encargado del restaurante, enlazado mediante una FK.
    """
    id: int = Field(default=None, primary_key=True)
    direccion: str = Field(max_length=100, nullable=False)
    codigo_postal: int = Field(nullable=False)
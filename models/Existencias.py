from sqlmodel import SQLModel, Field

class Existencias(SQLModel, table=True):
    """
    Representa un artículo en el inventario de existencias.
    
    Atributos
    ---------
    id : int
        Identificador único de la existencia (PK, Auto_Increment).
    precio_unidad : int
        Precio por unidad del artículo.
    nombre : str
        Nombre del artículo. Longitud máxima de 50 caracteres.
    cantidad : int
        Cantidad disponible del artículo.
    """
    id: int = Field(default=None, primary_key=True)
    precio_unidad: int = Field(nullable=False)
    nombre: str = Field(max_length=50, nullable=False)
    cantidad: int = Field(nullable=False)
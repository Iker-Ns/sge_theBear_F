from sqlmodel import SQLModel, Field

class Existencias(SQLModel, table=True):
    """
    Representa un artículo en el inventario de existencias.
    
    Atributos
    ---------
    id : int
        Identificador único de la existencia (PK, Auto_Increment).
    precio_unidad : int
        Precio por unidad del artículo. Este campo no puede ser nulo.
    nombre : str
        Nombre del artículo. Tiene una longitud máxima de 50 caracteres y no puede ser nulo.
    cantidad : int
        Cantidad disponible del artículo. Este campo es obligatorio.
    """
    id: int = Field(default=None, primary_key=True)
    precio_unidad: int = Field(nullable=False)
    nombre: str = Field(max_length=50, nullable=False)
    cantidad: int = Field(nullable=False)
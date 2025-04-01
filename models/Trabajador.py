from sqlmodel import SQLModel, Field

class Trabajador(SQLModel, table=True):
    """
    Representa un Trabajador.

    Atributos
    ---------
    id  : int
        Identificador del Trabajador (PK, Auto_Increment).
    seguridad_social : int
        Número de la seguridad social del Trabajador.
    nombre : str
        Nombre del Trabajador. Longitud máxima de 50 caracteres.
    apellido : str
        Apellido del Trabajador. Longitud máxima de 50 caracteres.
    cargo : str
        Cargo o posición del Trabajador. Longitud máxima de 50 caracteres.
    id_restaurante : int
        FK que referencia al Restaurante asociado.
    """
    id: int = Field(default=None, primary_key=True)
    seguridad_social: int = Field(nullable=False)
    nombre: str = Field(max_length=50, nullable=False)
    apellido: str = Field(max_length=50, nullable=False)
    cargo: str = Field(max_length=50, nullable=False)
    id_restaurante = Field(foreign_key="restaurante.id", nullable=False) # Trabajadores N .. 1 Restaurante
from sqlmodel import SQLModel, Field

class Trabajador(SQLModel, table=True):
    """
    Representa un Trabajador.
    
    Atributos:
        id (int): Identificador único del Trabajador. Es la clave primaria.
        seguridad_social (int): Número de la seguridad social del Trabajador. Campo obligatorio.
        nombre (str): Nombre del Trabajador. Valor obligatorio con una longitud máxima de 50 caracteres.
        apellido (str): Apellido del Trabajador. Valor obligatorio con una longitud máxima de 50 caracteres.
        cargo (str): Cargo o posición del Trabajador. Valor obligatorio con una longitud máxima de 50 caracteres.
        id_restaurante: Clave foránea que referencia al Restaurante asociado, indicando que varios Trabajadores pueden pertenecer a un mismo Restaurante.
    """
    id: int = Field(default=None, primary_key=True)
    seguridad_social: int = Field(nullable=False)
    nombre: str = Field(max_length=50, nullable=False)
    apellido: str = Field(max_length=50, nullable=False)
    cargo: str = Field(max_length=50, nullable=False)
    id_restaurante = Field(foreign_key="restaurante.id", nullable=False) # Trabajadores N .. 1 Restaurante
from sqlmodel import SQLModel, Field

class ProductosToCuenta(SQLModel, table=True):
    """
    Esta clase modela la relación N a N entre las entidades Cuenta y Existencias (Productos).
    
    Contiene los siguientes atributos:
        - id_cuenta: Entero que representa el identificador de la cuenta. Es clave primaria y clave externa que referencia a 'cuenta.id'.
        - id_producto: Entero que representa el identificador del producto. Es clave primaria y clave externa que referencia a 'existencias.id'.

    Se utiliza para gestionar la asociación entre una cuenta y los productos que tiene relacionados.
    """
    id_cuenta: int = Field(foreign_key="cuenta.id", primary_key=True, nullable=False) # ProductosToCuenta N .. N Cuenta
    id_producto: int = Field(foreign_key="existencias.id", primary_key=True, nullable=False) # ProductosToCuenta N -> N Existencias
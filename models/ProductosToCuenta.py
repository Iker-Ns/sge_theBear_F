from sqlmodel import SQLModel, Field

class ProductosToCuenta(SQLModel, table=True):
    """
    Representa la relación entre productos y cuentas.

    Atributos
    ---------
    - id_cuenta : int
        Identificador de la cuenta (PK, FK).
    - id_producto : int
        Identificador del producto (PK, FK).
    """
    id_cuenta: int = Field(foreign_key="cuenta.id", primary_key=True, nullable=False) # ProductosToCuenta N .. N Cuenta
    id_producto: int = Field(foreign_key="existencias.id", primary_key=True, nullable=False) # ProductosToCuenta N -> N Existencias
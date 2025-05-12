from sqlmodel import SQLModel, Field, Relationship

class Productos_To_Cuenta(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    cuenta_id: int = Field(foreign_key="cuenta.id", nullable=False)
    producto_id: int = Field(foreign_key="existencias.id", nullable=False)
    cantidad: int = Field(default=1)

    cuenta: "Cuenta" = Relationship(back_populates="productos_to_cuenta")
    existencias: "Existencias" = Relationship(back_populates="productos_to_cuenta")

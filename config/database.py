from os import getenv
from typing import Generator
from sqlmodel import Session, create_engine, SQLModel

class Database:
   """
   Permite conectar a la base de datos.

   Funciones
   ---------
   get_session() -> Generator[Session]
      Devuelve una sesión de conexión a la base de datos.
   """
   _uri = getenv("DATABASE_URI")
   _engine = create_engine(_uri)
   SQLModel.metadata.create_all(_engine) #Crea las tablas en la base de datos si no existen

   @staticmethod
   def get_session() -> Generator[Session]:
      session = Session(Database._engine)
      try:
         yield session
      finally:
         session.close()

   def __new__(cls):
      raise TypeError("This class cannot be instantiated")
from dotenv import load_dotenv
from os import getenv
from typing import Generator
from sqlmodel import Session, create_engine, SQLModel
import logging

class Database:
   """
   Permite conectar a la base de datos.

   Funciones
   ---------
   get_session() -> Generator[Session]
      Devuelve una sesión de conexión a la base de datos.
   """
   if getenv("DATABASE_URI") is None:
      logging.warning("No se ha encontrado la variable 'DATABASE_URI', cargando .Env...")
      load_dotenv()

   __uri = getenv("DATABASE_URI")
   __engine = create_engine(__uri)
   SQLModel.metadata.create_all(__engine) #Crea las tablas en la base de datos si no existen.

   @staticmethod
   def get_session() -> Generator[Session]:
      session = Session(Database.__engine)
      try:
         yield session
      finally:
         session.close()

   def __new__(cls):
      raise TypeError("Esta clase no se puede instanciar, usa get_session() para obtener una sesión de conexión a la base de datos.")
   
if __name__ == "__main__":
   # Solo para pruebas.
   session = Database.get_session()
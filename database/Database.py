from dotenv import load_dotenv
from os import getenv
from typing import Generator
from sqlmodel import Session, create_engine, SQLModel
import logging

class Database:
   """
   Permite conectarse a la base de datos.

   Funciones
   ---------
   get_session() -> Generator[Session]
      Devuelve una sesión de la base de datos.
   """
   if (__name__ == "__main__"):
      logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
      logging.debug("Cargando variables de entorno.")
      load_dotenv()
      logging.debug("Variables de entorno cargadas.")

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
   
# Solo para pruebas.
if __name__ == "__main__":
   session = Database.get_session()
   logging.debug("Conexión con la base de datos establecida.")
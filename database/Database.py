from dotenv import load_dotenv
from os import getenv
from typing import Generator
from sqlmodel import Session, create_engine, SQLModel
import logging

class Database:
    """
    Permite conectar a la base de datos.
    """
    # Inicialización de variables de clase
    __engine = None
    __uri = None

    @classmethod
    def init_db(cls):
        if cls.__engine is None:
            load_dotenv()
            cls.__uri = getenv("DATABASE_URI")

            if not cls.__uri:
                raise ValueError("DATABASE_URI no está configurada en .env")

            try:
                cls.__engine = create_engine(cls.__uri)
                SQLModel.metadata.create_all(cls.__engine)
                logging.info("Base de datos inicializada correctamente")
            except Exception as e:
                logging.error(f"Error al inicializar la base de datos: {e}")
                raise

    @classmethod
    def get_session(cls) -> Generator[Session, None, None]:
        if cls.__engine is None:
            cls.init_db()

        session = Session(cls.__engine)
        try:
            yield session
        finally:
            session.close()

    def __new__(cls):
        raise TypeError("Esta clase no se puede instanciar, usa get_session()")
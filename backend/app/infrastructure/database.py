from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Crea un archivo local llamado 'omnitask.db' en la raíz de tu backend
SQLALCHEMY_DATABASE_URL = "sqlite:///./omnitask.db"

# connect_args solo es necesario para SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """
    Función para abrir y cerrar la conexión a la base de datos 
    cada vez que la API reciba una petición.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
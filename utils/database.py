from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
import configparser
import os

config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "../config.ini")
config.read(config_path)
# config.read("../config.ini")

# Thay đổi URL này thành URL của utils của bạn
SQLALCHEMY_DATABASE_URL = config.get("database", "url")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db() -> Session:
    """
    Hàm này trả về một session SQLAlchemy.
    Sử dụng nó trong các dependency injection.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    get_db()


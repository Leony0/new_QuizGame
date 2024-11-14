#データベースを扱う処理

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# データベースのパス設定
DATABASE_DIR = os.path.join(os.path.dirname(__file__), "../database")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.join(DATABASE_DIR, 'fastapi_app.db')}"
#SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

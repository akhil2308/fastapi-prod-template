from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import *

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, #  connect_args={"check_same_thread": False}
    pool_size = DB_POOL_SIZE, 
    max_overflow = DB_MAX_OVERFLOW, 
    pool_recycle = 300,
    # pool_pre_ping=True, # for postgres
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
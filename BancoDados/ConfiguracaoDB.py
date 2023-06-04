from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URI = 'mysql+pymysql://root:root@localhost/papelaria'

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

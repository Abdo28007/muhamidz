
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

url = "mysql+pymysql://seraiche_abderrahmen:ABDO20032020abdo@localhost/muhami"
engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
 
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



Base.metadata.create_all(engine)

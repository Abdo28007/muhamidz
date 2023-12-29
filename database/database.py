from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'mysql+pymysql://root:nightlake@localhost:3306/mouhamiapp'
engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
 
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Check if the connection to the database is successful
try:
    engine.connect()
    print("Successfully connected to the database")
except Exception as e:
    print(f"Error connecting to the database: {e}")



Base.metadata.create_all(engine)

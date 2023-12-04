# database.py

from sqlalchemy import create_engine, Column, Integer, String, MetaData
from databases import Database
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+aiomysql://user:password@localhost/db_name"

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base(metadata=metadata)

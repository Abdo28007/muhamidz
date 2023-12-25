from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, Sequence, ForeignKey, func
from database import engine

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()




class CategorieModel(Base):
    __tablename__ = "categories_avocat"
    id = Column(Integer,Sequence("categorie_id_seq"), primary_key=True, index=True)
    caegorie_name = Column(String(255),index=True)
    description = Column(String(255))





Base.metadata.create_all(engine)
from sqlalchemy import  Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from database import engine


class CategorieModel(Base):
    __tablename__ = "categories_avocat"
    id = Column(Integer, primary_key=True, index=True)
    caegorie_name = Column(String(255),index=True)
    description = Column(String(255))



Base.metadata.create_all(engine)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, Sequence, ForeignKey, func
from database import engine
from models import LawyerModel as lawyer
from models import UserModel as user






Base = declarative_base()
class AvisModel(Base):
    __tablename__ = "avis"

    id = Column(Integer, Sequence("avis_id_seq"), primary_key=True, index=True)
    commentaire = Column(String(255),default = None)
    rating = Column(Integer,nullable = False)
    publication_date = Column(Date)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


    

Base.metadata.create_all(engine)
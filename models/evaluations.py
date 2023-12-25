from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, Sequence, ForeignKey, func
from database import engine
from models.user import  UserModel
from models.lawyer import LawyerModel

from sqlalchemy.orm import relationship




Base = declarative_base()
class EvaluationModel(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)
    commentaire = Column(String(255),default = None)
    rating = Column(Integer,nullable = False)
    publication_date = Column(Date)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

Base.metadata.create_all(engine)

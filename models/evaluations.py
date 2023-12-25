from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, Sequence, ForeignKey, func
from database import engine
from models.user import  UserModel
from models.lawyer import LawyerModel
from datetime import datetime
from sqlalchemy.orm import relationship
from pydantic import BaseModel  



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

class EvaluationCreate(BaseModel):
    commentaire: str
    rating: int
    publication_date: datetime
    user_id: int
    lawyer_id: int
class EvaluationUpdate(BaseModel):
    commentaire: str
    rating: int
    publication_date: datetime
    user_id: int
    lawyer_id: int
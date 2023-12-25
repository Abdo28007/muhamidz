from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column, Integer, String, Date, DateTime,Sequence
from datetime import datetime 
from database import engine
from sqlalchemy.orm import relationship


Base = declarative_base()
class LawyerModel(Base):
    __tablename__ = "lawyers"

    id = Column(Integer, Sequence("lawyer_id_seq"), primary_key=True, index=True)
    fullname = Column(String(255), index=True)
    email = Column(String(50), unique=True, index=True)
    languages= Column(String(255))
    gendre = Column(String(10))
    phone_number = Column(String(255))
    address = Column(String(255))
    city = Column(String(255))
    description = Column(String(255))
    password = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    

Base.metadata.create_all(engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column, Integer, String, Date, DateTime
from datetime import datetime 
from database import engine
from sqlalchemy.orm import relationship
from pydantic import BaseModel , EmailStr

Base = declarative_base()
class LawyerModel(Base):
    __tablename__ = "lawyers"

    id = Column(Integer, primary_key=True, index=True)
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

class LawyerCreate(BaseModel):
    fullname: str
    email: EmailStr
    languages: str
    gendre: str
    phone_number: str
    address: str
    city: str
    description: str
    password : str

class LawyerUpdate(BaseModel):
    fullname: str
    email: EmailStr
    languages: str
    gendre: str
    phone_number: str
    address: str
    city: str
    description: str
    password : str
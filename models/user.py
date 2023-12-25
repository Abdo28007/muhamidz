from sqlalchemy import Column, Integer, String,DateTime
from database import engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy.orm import relationship


Base = declarative_base()
class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(255))
    email = Column(String(255), index=True)
    password = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(engine)

class UserCreate(BaseModel):
    fullname: str
    email: str
    password: str


class UserUpdate(BaseModel):
    fullname: str
    email: str
    password: str

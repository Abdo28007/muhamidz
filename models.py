# models.py

from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    age = Column(Integer)
# models.py

class UserResponse(Base):
    username: str
    email: str
    full_name: str
    age: int

from sqlalchemy import Column, Integer, String, Sequence,DateTime
from sqlalchemy.orm import relationship
from database import engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()





class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True, index=True)
    fullname = Column(String(255))
    email = Column(String(255), index=True)
    password = Column(String(255))



    










Base.metadata.create_all(engine)
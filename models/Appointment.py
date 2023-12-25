from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, Sequence, ForeignKey, func,Boolean
from database import engine
from sqlalchemy.orm import relationship


from models import UserModel as users
from models import LawyerModel as lawyers



Base = declarative_base()
class AppointmentModel(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    appointment_time = Column(DateTime, nullable=True)
    accepted = Column(Boolean, default=False)





    
Base.metadata.create_all(engine)
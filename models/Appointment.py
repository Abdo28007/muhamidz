from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column, Integer, String, DateTime, ForeignKey,Boolean
from sqlalchemy.orm import relationship


from database import engine



Base = declarative_base()
class AppointmentModel(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    appointment_time = Column(DateTime, nullable=True)
    accepted = Column(Boolean, default=False)


Base.metadata.create_all(engine)


    

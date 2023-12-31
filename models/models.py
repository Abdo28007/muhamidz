from sqlalchemy import Column, Integer, String,DateTime , LargeBinary , ForeignKey , Date , func , Boolean , Float
from datetime import datetime
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Boolean



class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(255))
    email = Column(String(255), index=True)
    password = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    


    #relationships
    image = relationship("ImageModel", back_populates="user")
    evaluations = relationship("EvaluationModel", back_populates = 'user')
    appointments = relationship("AppointmentModel", back_populates="user")


class ImageModel(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), index=True)
    data = Column(LargeBinary)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("UserModel", back_populates="image")
    



class LawyerModel(Base):
    __tablename__ = "lawyers"
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(255), index=True)
    email = Column(String(50), unique=True, index=True)
    password = Column(String(255))
    languages= Column(String(255))
    phone_number = Column(String(255))
    address = Column(String(255))
    city = Column(String(255))
    gendre = Column(String(10))
    description = Column(String(255))
    rating = Column(Float , default = 0)
    is_active = Column(Boolean , default = False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


    #relationships
    evaluations = relationship("EvaluationModel", back_populates = 'lawyer')
    categories = relationship("CategorieModel",secondary = "lawyer_category", back_populates="lawyers")
    # relationship with appointments and availability
    availabilities = relationship("LawyerAvailabilityModel", back_populates="lawyer")
    appointments = relationship("AppointmentModel", back_populates="lawyer")



class EvaluationModel(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    commentaire = Column(String(255),default = None)
    rating = Column(Integer,nullable = False)
    user_id = Column(Integer,ForeignKey('users.id'),index=True)
    lawyer_id = Column(Integer,ForeignKey('lawyers.id'))  

    publication_date = Column(DateTime , default=func.now())
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Relationships
    user = relationship("UserModel", back_populates = 'evaluations')
    lawyer = relationship("LawyerModel", back_populates = 'evaluations')

    def __init__(self, commentaire, rating, user_id, lawyer_id):
        self.commentaire = commentaire
        self.rating = rating
        self.user_id = user_id
        self.lawyer_id = lawyer_id




class CategorieModel(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    caegorie_name = Column(String(255),index=True)
    description = Column(String(255))

    #relationships
    lawyers = relationship("LawyerModel",secondary = "lawyer_category", back_populates="categories")




class CategorieLawyer(Base):
    __tablename__ = "lawyer_category"

    Lawyer_id = Column(Integer, ForeignKey('lawyers.id', ondelete='CASCADE'),primary_key=True)
    category_id = Column(Integer,ForeignKey('categories.id',ondelete="CASCADE"),primary_key=True)




class AppointmentModel(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    appointment_time = Column(DateTime, nullable=True)
    accepted = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    lawyer_id = Column(Integer, ForeignKey("lawyers.id"), index=True)
    time_availability_id = Column(Integer, ForeignKey("lawyer_availabilities.id"), index=True)

    # Relationships
    user = relationship("UserModel", back_populates="appointments")
    lawyer = relationship("LawyerModel", back_populates="appointments")



class LawyerAvailabilityModel(Base):
    __tablename__ = "lawyer_availabilities"

    id = Column(Integer, primary_key=True, index=True)
    lawyer_id = Column(Integer, ForeignKey("lawyers.id"), index=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    is_available = Column(Boolean, default=True)  # New column to track availability status

    # Relationship
    lawyer = relationship("LawyerModel", back_populates="availabilities")


    







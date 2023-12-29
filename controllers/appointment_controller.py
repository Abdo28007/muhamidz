from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import *
from datetime import datetime
from controllers.appointment_controller import *
from models.schema import *


# controller.py

from sqlalchemy.orm import Session
from models import AppointmentModel

def request_appointment(db: Session,appointment_request:AppointmentRequest):
    appointment = AppointmentModel(user_id=appointment_request.user_id, lawyer_id=appointment_request.lawyer_id, time_availability_id=appointment_request.time_availability_id ,appointment_time=appointment_request.appointment_time)
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment

def accept_appointment(db: Session, appointment_id: int, time_availability_id: int):
    appointment = db.query(AppointmentModel).filter(AppointmentModel.id == appointment_id).first()
    
    if appointment:
        lawyer_availability = db.query(LawyerAvailabilityModel).filter(LawyerAvailabilityModel.id == time_availability_id).first()

        if lawyer_availability:
            appointment.appointment_time = lawyer_availability.start_time
            appointment.accepted = True
            lawyer_availability.is_available = False
            db.commit()
            return appointment
            
    return None

def delete_appointment(db: Session, appointment_id: int):
    appointment = db.query(AppointmentModel).filter(AppointmentModel.id == appointment_id).first()
    if appointment:
        db.delete(appointment)
        db.commit()
        return True
    return False

def get_user_appointments(db: Session, user_id: int):
    appointments = db.query(AppointmentModel).filter(AppointmentModel.user_id == user_id).all()
    return appointments

def get_lawyer_appointments(db: Session, lawyer_id: int):
    appointments = db.query(AppointmentModel).filter(AppointmentModel.lawyer_id == lawyer_id).all()
    return appointments

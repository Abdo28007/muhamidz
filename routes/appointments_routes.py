from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from controllers.appointment_controller import *
from models.schema import *

appointment_route = APIRouter()

@appointment_route.post("/appointment/request", response_model=AppointmentResponse)
async def request_appointment_route(
    appointment_data: AppointmentRequest,
    db: Session = Depends(get_db)
):
    
    appointment = request_appointment(
        db,
        appointment_request = appointment_data
    )
    return {"message": "Appointment requested successfully", "data": appointment_data}

@appointment_route.post("/appointments/{appointment_id}/accept")
def accept_appointment_route(appointment_id: int, time_availability_id: int, db: Session = Depends(get_db)):
    appointment = accept_appointment(db, appointment_id, time_availability_id)

    if appointment:
        return {"message": "Appointment accepted successfully."}

    raise HTTPException(status_code=404, detail="Appointment not found.")

@appointment_route.delete("/appointment/delete/{appointment_id}", response_model=dict)
async def delete_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_appointment(db, appointment_id)
    if deleted:
        return {"message": "Appointment deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Appointment not found")

@appointment_route.get("/appointments/user/{user_id}", response_model=list[AppointmentResponse])
async def get_user_appointments(
    user_id: int,
    db: Session = Depends(get_db)
):
    appointments = get_user_appointments(db, user_id)
    return appointments

@appointment_route.get("/appointments/lawyer/{lawyer_id}", response_model=list[AppointmentResponse])
async def get_lawyer_appointments_route(
    lawyer_id: int,
    db: Session = Depends(get_db)
):
    appointments = get_lawyer_appointments(db, lawyer_id)
    return appointments

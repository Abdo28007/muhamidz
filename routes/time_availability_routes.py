# routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from controllers.lawyer_availability_controller import *
from models.schema import *
import bcrypt
from datetime import datetime
from models import *
from controllers import *

time_availability_route = APIRouter()

@time_availability_route.post("/availability/create", response_model=AvailabilityResponse)
async def create_availability_route(
    availability_data: LawyerAvailabilityCreate,
    db: Session = Depends(get_db)
):
    availability = create_availability(
        db,
        lawyer_id=availability_data.lawyer_id,
        start_time=availability_data.start_time,
        end_time=availability_data.end_time
    )
    return {"message": "Availability created successfully", "data": availability_data}

@time_availability_route.delete("/availability/delete/{availability_id}", response_model=dict)
async def delete_availability_route(
    availability_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_availability(db, availability_id)
    if deleted:
        return {"message": "Availability deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Availability not found")

@time_availability_route.get("/availability/{lawyer_id}/list")
def get_time_availabilities_route(lawyer_id: int, db: Session = Depends(get_db)):
    availabilities = get_time_availabilities(db, lawyer_id)
    if not availabilities:
        raise HTTPException(status_code=404, detail="No availabilities found for the specified lawyer")
    return availabilities

from sqlalchemy.orm import Session
from models import LawyerAvailabilityModel
from datetime import datetime
from typing import List

def create_availability(db: Session, lawyer_id: int, start_time: datetime, end_time: datetime):
    availability = LawyerAvailabilityModel(lawyer_id=lawyer_id, start_time=start_time, end_time=end_time)
    db.add(availability)
    db.commit()
    db.refresh(availability)
    return availability

def delete_availability(db: Session, availability_id: int):
    availability = db.query(LawyerAvailabilityModel).filter(LawyerAvailabilityModel.id == availability_id).first()
    if availability:
        db.delete(availability)
        db.commit()
        return True
    return False

def get_time_availabilities(db: Session, lawyer_id: int) -> List[LawyerAvailabilityModel]:
    availabilities = db.query(LawyerAvailabilityModel).filter(LawyerAvailabilityModel.lawyer_id == lawyer_id).all()
    return availabilities




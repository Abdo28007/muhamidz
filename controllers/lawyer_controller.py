import bcrypt
from sqlalchemy.orm import Session
from models import LawyerModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from datetime import datetime 
LawyerCreateResponse = sqlalchemy_to_pydantic(LawyerModel, exclude=['id','password'])


def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def create_lawyer_account(
    db: Session,
    fullname: str,
    email: str,
    languages: str,
    gendre: str,
    phone_number: str,
    address: str,
    city: str,
    description: str,
    password : str
) -> LawyerCreateResponse:
    # Create a new lawyer instance
    hashed_password = hash_password(password)
    new_lawyer = LawyerModel(
        fullname=fullname,
        email=email,
        languages=languages,
        gendre=gendre,
        phone_number=phone_number,
        address=address,
        city=city,
        description=description,
        password = hashed_password
    )

    # Add the new lawyer to the database
    db.add(new_lawyer)
    db.commit()
    db.refresh(new_lawyer)

    return LawyerCreateResponse.from_orm(new_lawyer)

def get_lawyer_by_email(db: Session, email: str) -> LawyerCreateResponse:
    lawyer = db.query(LawyerModel).filter(LawyerModel.email == email).first()
    return LawyerCreateResponse.from_orm(lawyer) if lawyer else None


def update_lawyer(
    db: Session,
    lawyer_id: int,
    fullname: str,
    email: str,
    languages: str,
    gendre: str,
    phone_number: str,
    address: str,
    city: str,
    description: str
) -> LawyerCreateResponse:
    # Check if the lawyer with the specified ID exists
    existing_lawyer = db.query(LawyerModel).filter(LawyerModel.id == lawyer_id).first()

    # Update the lawyer's information
    existing_lawyer.fullname = fullname
    existing_lawyer.email = email
    existing_lawyer.languages = languages
    existing_lawyer.gendre = gendre
    existing_lawyer.phone_number = phone_number
    existing_lawyer.address = address
    existing_lawyer.city = city
    existing_lawyer.description = description
    existing_lawyer.updated_at = datetime.utcnow()

    # Commit the changes to the database
    db.commit()
    db.refresh(existing_lawyer)

    return LawyerCreateResponse.from_orm(existing_lawyer)
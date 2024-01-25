from fastapi import Depends , File , UploadFile

from sqlalchemy.orm import Session
import bcrypt
from fastapi.responses import JSONResponse
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from controllers.auth_controller import *
from models import *
from dotenv import dotenv_values
config = dotenv_values('.env')
import secrets

async def generate_unique_id():
    return f"{secrets.randbelow(10**8):08d}"
async def create_user_account(db: Session,user_data : UserCreate):
    hashed_password =  hash_password(user_data.password)
    _id =  await generate_unique_id()
    db_user = UserModel(id = _id,fullname=user_data.fullname, email=user_data.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



async def request_appoinement(db : Session,user_id : int , lawyer_id : int ,appointment_data : AppointmentRequest):
    _id =  await generate_unique_id()
    appoinement = AppointmentModel(
        appoinement_id = _id,
        user_id = user_id,
        lawyer_id = lawyer_id,
        description = appointment_data.description,
        appointment_time = appointment_data.appointment_time
    )
    db.add(appoinement) 
    db.commit()
    db.refresh(appoinement)
    return appoinement



async def update_user (db: Session,user_id :int,user_data :UserCreate):
    # Check if the user with the specified ID exists
    existing_user = db.query(UserModel).filter(UserModel.id ==user_id).first()
    # Update the lawyer's information
    existing_user.fullname = user_data.fullname
    existing_user.email = user_data.email
    existing_user.updated_at = datetime.utcnow()
    # Commit the changes to the database
    db.commit()
    db.refresh(existing_user)
    return existing_user



async def delete_user(db: Session,user_id: int ):
    # Check if the user with the specified ID exists
    existing_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    # Delete the user from the database
    db.delete(existing_user)
    db.commit()
    return existing_user






async def user_rate(db :Session,user_id : int,lawyer_id :int,commentaire : str,rating :int):
    _id = await generate_unique_id()
    rate = EvaluationModel(id = _id ,commentaire = commentaire , rating = rating ,user_id= user_id,lawyer_id= lawyer_id)
    db.add(rate)
    db.commit()
    db.refresh(rate)
    return rate



async def google_auth():
    pass
    return rate
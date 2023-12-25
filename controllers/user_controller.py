# controllers/user_controller.py
from sqlalchemy.orm import Session
from models.user import *
import bcrypt
from datetime import datetime
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from dotenv import load_dotenv
load_dotenv()
from fastapi.responses import JSONResponse



UserUpdateResponse = sqlalchemy_to_pydantic(UserModel, exclude=['id','password'])
def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def create_user_account(db: Session,user_data : UserCreate):
    hashed_password = hash_password(user_data.password)
    db_user = UserModel(fullname=user_data.fullname, email=user_data.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db : Session):
    users = db.query(UserModel).all()
    return  JSONResponse(content =users)

def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

def update_user (
    db: Session,
    user_id :int,
    user_data :UserUpdate
)-> UserUpdateResponse :
    # Check if the user with the specified ID exists
    existing_user = db.query(UserModel).filter(UserModel.id ==user_id).first()
    # Update the lawyer's information
    existing_user.fullname = user_data.fullname
    existing_user.email = user_data.email
    existing_user.updated_at = datetime.utcnow()
    # Commit the changes to the database
    db.commit()
    db.refresh(existing_user)
    return UserUpdateResponse.from_orm(existing_user) 

def delete_user(db: Session, user_id: int):
    # Check if the user with the specified ID exists
    existing_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    # Delete the user from the database
    db.delete(existing_user)
    db.commit()
    return existing_user

def user_login_controller(db:Session,email:str , password :str):

    return None
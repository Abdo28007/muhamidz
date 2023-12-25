# controllers/user_controller.py
from sqlalchemy.orm import Session
from models.user import UserModel
import bcrypt
from datetime import datetime
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
UserUpdateResponse = sqlalchemy_to_pydantic(UserModel, exclude=['id','password'])
def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


    
def create_user_account(db: Session, fullname: str, email: str, password: str):
    hashed_password = hash_password(password)
    db_user = UserModel(fullname=fullname, email=email,password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db : Session):
    return db.query(UserModel).all()


def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

def update_user (
    db: Session,
    user_id: int,
    fullname: str,
    email: str
)-> UserUpdateResponse :
    # Check if the user with the specified ID exists
    existing_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    # Update the lawyer's information
    existing_user.fullname = fullname
    existing_user.email = email
    existing_user.updated_at = datetime.utcnow()
    # Commit the changes to the database
    db.commit()
    db.refresh(existing_user)
    return UserUpdateResponse.from_orm(existing_user) 
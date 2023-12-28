# controllers/user_controller.py
from sqlalchemy.orm import Session
from models import *
from controllers.auth_controller import *
import bcrypt
from datetime import datetime
from fastapi.responses import JSONResponse
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
UserUpdateResponse = sqlalchemy_to_pydantic(UserModel, exclude=['id','password'])
from fastapi import Depends , File , UploadFile






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




def get_user_by_id(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()



def update_user (
    db: Session,
    user_id :int,
    user_data :UserCreate 
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





def delete_user(db: Session, 
                user_id: int,
                user : UserModel = Depends(get_current_user)
                ):
    # Check if the user with the specified ID exists
    existing_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if existing_user.id != user_id :
        raise HTTPException(
            status_code = 401,
            detail = 'unothorized'
        )
    # Delete the user from the database
    db.delete(existing_user)
    db.commit()
    return existing_user

def user_rate(
        db :Session,
        user_id : int,
        lawyer_id :int,
        commentaire : str,
        rating :int
    ):
    rate = EvaluationModel(commentaire , rating ,user_id,lawyer_id)
    db.add(rate)
    db.commit()
    db.refresh(rate)
    return rate
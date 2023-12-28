from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt , JWTError
from datetime import datetime, timedelta
from models import *
import bcrypt
from sqlalchemy.orm import Session
from pydantic_sqlalchemy import sqlalchemy_to_pydantic




UserResponse = sqlalchemy_to_pydantic(UserModel, exclude=['password'])
LawyerResponse = sqlalchemy_to_pydantic(LawyerModel, exclude=['password'])


def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

SECRET_KEY = "77aae4bc1f13cce97dd4d2888ccafeb1143aff464ab6f3819b57b49b8f0f40e1"
ALGORITHM = "HS512"

async def authenticate_user(email: str, password: str, db: Session):
    user = db.query(UserModel).filter(UserModel.email == email).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail ="account does not exist create account"
        ) 
    if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        raise HTTPException(
            status_code=404,
            detail ="password do not match try again"
        ) 
    access_token = jwt.encode(
        {
         "user_email": user.email,
         "user_name" : user.fullname,
         "user_id" : user.id,
         "expired_in": 5},
        SECRET_KEY,
        algorithm=ALGORITHM,
    )
    return access_token






async def authenticate_lawyer(email: str, password: str, db: Session):
    lawyer = db.query(LawyerModel).filter(LawyerModel.email == email).first()
    if not lawyer:
        raise HTTPException(
            status_code=404,
            detail ="account does not exist create account"
        ) 
    if not bcrypt.checkpw(password.encode('utf-8'), lawyer.password.encode('utf-8')):
        raise HTTPException(
            status_code=404,
            detail ="password do not match try again"
        ) 
    access_token = jwt.encode(
        
        {"lawyer_email": lawyer.email,
         "lawyer_id" : lawyer.id,
         "lawyer_name" : lawyer.fullname,
         "expired_in": 10},
        SECRET_KEY,
        algorithm=ALGORITHM,
    )
    return access_token




# Define the function to get the current user
async def get_current_user(db : Session ,token: str = Depends(authenticate_user))-> UserResponse :
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise HTTPException(
                status_code = 401 ,
                detail =' invalid acces token'
            )
    except JWTError:
        raise HTTPException(
                status_code = 401 ,
                detail =' invali acces token'
        )
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    return user





async def get_current_lawyer(db : Session ,token: str = Depends(authenticate_lawyer))-> LawyerResponse :
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        lawyer_id: str = payload.get("lawyer_id")
        if lawyer_id is None:
            raise HTTPException(
                status_code = 401 ,
                detail =' invalid acces token'
            )
    except JWTError:
        raise HTTPException(
                status_code = 401 ,
                detail =' invali acces token'
        )
    lawyer = db.query(LawyerModel).filter(LawyerModel.id == lawyer_id).first()
    return lawyer

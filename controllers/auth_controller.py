from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt , JWTError
from datetime import datetime, timedelta
from models import *
import bcrypt
from sqlalchemy.orm import Session
from dotenv import   dotenv_values
config = dotenv_values('.env')




def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')







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



async def authenticate(email : str , password : str , db : Session):
    try:
        expiration_time = str(datetime.utcnow() + timedelta(days=2))
        
        lawyer =  db.query(LawyerModel).filter(LawyerModel.email == email).first()
        if not lawyer : 
            user =   db.query(UserModel).filter(UserModel.email == email).first()
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
                {"user_email": user.email,
                "user_id" : user.id,
                "user_name" : user.fullname,
                "is_lawyer": False,
                "expired_in": expiration_time.timestamp()},
            config['SECRET_KEY'],
            algorithm=config['ALGORITHM'])
            return access_token
        if not bcrypt.checkpw(password.encode('utf-8'), lawyer.password.encode('utf-8')):
            raise HTTPException(
                status_code=404,
                detail ="password do not match try again"
                ) 
        access_token = jwt.encode(
            {"user_email": lawyer.email,
            "user_id" : lawyer.id,
            "user_name" : lawyer.fullname,
            "is_lawyer" : True,
             "expired_in": expiration_time.timestamp()},
        config['SECRET_KEY'],
        algorithm=config['ALGORITHM'])
        return access_token
    except Exception as e :
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")





async def get_current_user(db : Session ,token: str = Depends(authenticate)) :
    try:
        
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise HTTPException(
                status_code = 401 ,
                detail =' invalid acces token'
            )
        is_lawyer = payload.get('is_lawyer')
        if is_lawyer:
                lawyer = db.query(LawyerModel).filter(LawyerModel.id == lawyer_id).first()
                return lawyer
        user = db.query(UserModel).filter(UserModel).first()
        return user
    except JWTError:
        raise HTTPException(
                status_code = 401 ,
                detail =' invali acces token'
        )
    









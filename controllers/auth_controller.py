from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt , JWTError
from datetime import datetime, timedelta
from models import *
import bcrypt
from sqlalchemy.orm import Session
from dotenv import   dotenv_values
config = dotenv_values('.env')


from fastapi_mail import ConnectionConfig , FastMail , MessageSchema ,MessageType


conf = ConnectionConfig(
            MAIL_USERNAME = "muhamidz52@gmail.com",
            MAIL_PASSWORD = "frzy iypa dyau btir",
            MAIL_FROM = "muhamidz52@gmail.com",
            MAIL_PORT = 587,
            MAIL_SERVER = "smtp.gmail.com",
            MAIL_STARTTLS = True,
            MAIL_SSL_TLS = False,
            USE_CREDENTIALS = True,
            VALIDATE_CERTS = True
        )




def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed_password =  bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')



async def authenticate(email : str , password : str , db : Session):
    try:
        expiration_time = datetime.utcnow() + timedelta(days =2)
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
            "77aae4bc1f13cce97dd4d2888ccafeb1143aff464ab6f3819b57b49b8f0f40e1",
            algorithm="HS256")
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
        "77aae4bc1f13cce97dd4d2888ccafeb1143aff464ab6f3819b57b49b8f0f40e1",
        algorithm="HS256")
        return access_token
    except Exception as e :
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


async def get_current_user(db : Session ,token: str = Depends(authenticate)) :
    try: 
        payload = await jwt.decode(token, "77aae4bc1f13cce97dd4d2888ccafeb1143aff464ab6f3819b57b49b8f0f40e1", algorithms=["HS256"])
        exp_timestamp = payload['expired_in']
        exp_datetime = datetime.fromtimestamp(exp_timestamp, timezone.utc)
        if exp_datetime.timestamp() < exp_timestamp :
            raise HTTPException(
                status_code = 422,
                detail = "Token has Expired"
                )
        is_lawyer = payload['is_lawyer']
        if is_lawyer:
                user = db.query(LawyerModel).filter(LawyerModel.id == lawyer_id).first()
        user = db.query(UserModel).filter(UserModel).first()
        return user
    except JWTError as e:
        raise HTTPException(
                status_code = 401 ,
                detail =f"invali acces token{str(e)}"
        )
    


async def send_email_reset_password(db : Session , email : str):
    expiration_time = datetime.utcnow() + timedelta(minutes=5)
    user = db.query(UserModel).filter(UserModel.email==email).first()
    if not user:
        lawyer = db.query(LawyerModel).filter(LawyerModel.email == email).first()
        if not lawyer:
            raise UserNotFound("This Email is Not Registerd")
        token =  await jwt.encode(
        {
         "user_id" : lawyer.id,
         "is_lawyer" : True,
         "expired_in": expiration_time.timestamp()},

        "77aae4bc1f13cce97dd4d2888ccafeb1143aff464ab6f3819b57b49b8f0f40e1",
        algorithm="HS256",
        )
        user_mail = lawyer.email
    else :
        token =  await jwt.encode(
                {
                "user_id" : user.id,
                "is_lawyer" : False,
                "expired_in": expiration_time.timestamp()},
                "77aae4bc1f13cce97dd4d2888ccafeb1143aff464ab6f3819b57b49b8f0f40e1",
                algorithm="HS256",
                )
        user_mail = user.email
        
    link = f"http://localhost:8000/reset-password-email/{token}"
    html = f"""
            <p>Click here to reset your password </p>
            <center>
                <a href="{link}">
                    <button style="background-color: blue; color: white; padding: 10px 20px; border-radius: 5px; font-size: 16px;">Click Here</button>
                </a>
            </center>
        """
    message = MessageSchema(
            subject="Fastapi-Mail module",
            recipients=[user_mail],
            body=html,
            subtype=MessageType.html
            )
    
    mail =  FastMail(conf)
    try:
        await mail.send_message(message)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


async def change_password(db : Session , user_email : str , resetPassword_info : resetPassword):
    user = db.query(UserModel).filter(UserModel.email == user_email).first()
    if not user:
        lawyer = db.query(LawyerModel).filter(LawyerModel.email== user_email).first()
        print(lawyer)
        if not lawyer:
            raise HTTPException(
                status_code = 404,
                detail = "This Email is Not Registerd")
        if not bcrypt.checkpw(resetPassword_info.old_password.encode('utf-8'), lawyer.password.encode('utf-8')):
            raise HTTPException(
                status_code=404,
                detail ="password do not match try again"
                )
        lawyer.password =  hash_password(resetPassword_info.new_password)
        db.commit()
        db.refresh(lawyer)
        return {"message":"password changes succesfully"}
    if not bcrypt.checkpw(resetPassword_info.old_password.encode('utf-8'), user.password.encode('utf-8')):
        raise HTTPException(
            status_code=404,
            detail ="password do not match try again"
            )
    user.password =  hash_password(resetPassword_info.new_password)
    db.commit()
    db.refresh(user)
    return {"message":"password changes succesfully"}





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
            MAIL_USERNAME = config['GMAIL'],
            MAIL_PASSWORD =  config['GMAIL_SECRET'],
            MAIL_FROM = config['GMAIL'],
            MAIL_PORT = 587,
            MAIL_SERVER = "smtp.gmail.com",
            MAIL_STARTTLS = True,
            MAIL_SSL_TLS = False,
            USE_CREDENTIALS = True,
            VALIDATE_CERTS = True
        )



def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


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
    



async def send_email_reset_password(db : Session , email : str):
    expiration_time = datetime.utcnow() + timedelta(minutes=5)
    user = db.query(UserModel).filter(UserModel.email==email).first()
    if not user:
        lawyer = db.query(LawyerModel).filter(LawyerModel.email == email).first()
        if not lawyer:
            raise UserNotFound("This Email is Not Registerd")
        token =  jwt.encode(
        {
         "user_id" : lawyer.id,
         "is_lawyer" : True,
         "expired_in": expiration_time.timestamp()},

        config['SECRET_KEY'],
        algorithm=config['ALGORITHM'],
        )
        user_mail = lawyer.email
    else :
        token =  jwt.encode(
                {
                "user_id" : user.id,
                "is_lawyer" : False,
                "expired_in": expiration_time.timestamp()},
                config['SECRET_KEY'],
                algorithm=config['ALGORITHM'],
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








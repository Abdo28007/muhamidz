from fastapi import APIRouter, Depends, HTTPException , Response 
from sqlalchemy.orm import Session
import bcrypt
from datetime import datetime
from database import get_db 
from models import *
from controllers import *
from jose import jwt , JWTError
from dotenv import   dotenv_values
config = dotenv_values('.env')

auth_route = APIRouter() 



@auth_route.post("/login")
async def login(user_info :LoginData , db : Session = Depends(get_db)):
    try:

        print(config['GMAIL'])
        access_token = await authenticate(db =db,email = user_info.email,password = user_info.password )
        
        return {"access token " : access_token }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")



@auth_route.post('/forget_password')
async def forget_password(email : str , db : Session= Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email==email).first()
    if not user:
        lawyer = db.query(LawyerModel).filter(LawyerModel.email==email).first()
        if lawyer is None:
            raise HTTPException(status_code=404,detail="This email does not exist.")
    send_email = await send_email_reset_password(db , email)
    if send_email:
        return{"msg":'A link to reset your password has been sent to your email.'}




@auth_route.post('/reset-password-email/{token}')
async def reset_password(password : str , token : str , db :Session=Depends(get_db)):
    hashed_password = hash_password(password)
    decoded_token = await jwt.decode(token, config['SECRET_KEY'], algorithms=["HS256"])
    exp_timestamp = decoded_token['expired_in']
    exp_datetime = datetime.fromtimestamp(exp_timestamp, timezone.utc)
    if exp_datetime.timestamp() < exp_timestamp :
        raise HTTPException(
                status_code = 422,
                detail = "Token has Expired"
            )
    user_id = decoded_token['user_id']
    is_lawyer = decoded_token['is_lawyer'] 
    if is_lawyer:
        user = db.query(LawyerModel).filter(LawyerModel.id == user_id).first()
    else:
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
    user.password = hashed_password
    db.commit()
    db.refresh(user)
    return {"msg": "password reset successfully",
            'data':user}

    
from fastapi import APIRouter, Depends, HTTPException , Response , File , UploadFile
from sqlalchemy.orm import Session
import bcrypt
from datetime import datetime
from database import get_db 
from models import *
from controllers import *
from jose import jwt , JWTError
from dotenv import   dotenv_values
from fastapi.staticfiles import StaticFiles
import os
import secrets
from PIL import Image




auth_route = APIRouter() 
config = dotenv_values('.env')
auth_route.mount("/static", StaticFiles(directory= "static"),name="static")






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

    
@auth_route.put("/{user_email}/update-password")
async def update_password(user_email : str,resetPassword_info: resetPassword , db : Session = Depends(get_db)):
    updated_password = await change_password(db= db ,user_email = user_email , resetPassword_info= resetPassword_info)
    return updated_password




@auth_route.post("/{user_id}/profile/picture")
async def create_profile_picture(user_id : int ,file : UploadFile = File(...), db :Session =Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    FILEPATH = "static/users/"
    if not  user :
        user= db.query(LawyerModel).filter(LawyerModel.id == user_id).first()
        FILEPATH = "static/lawyers/"
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
    filename = file.filename
    extention = filename.split(".")
    extention = extention[-1]
    if extention not in ["jpeg", "png","jpg","gif"]:
        raise HTTPException(status_code=400, detail="Unsupported file")
    token_name = secrets.token_hex(16) + "."+ extention
    generated_name = FILEPATH + token_name
    file_content = await file.read()
    with open(generated_name, "wb+") as file:
        file.write(file_content)
    #resize the picture:
    img = Image.open(generated_name)
    img = img.resize(size = (200,200))
    img.save(generated_name)
    file.close()
    user.image = token_name
    db.commit()
    db.refresh(user)
    return {"filename": token_name}  


@auth_route.patch("/{user_id}/profile/picture/update")
async def update_profile_picture(user_id : int ,file : UploadFile = File(...), db :Session =Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user :
        if not user.image:
            raise HTTPException(status_code=404, detail="Image not found")
        FILEPATH = "static/users/"
        os.remove("static/users/"+user.image)
    if not  user :
        user= db.query(LawyerModel).filter(LawyerModel.id == user_id).first()
        if user :
            if not user.image:
                raise HTTPException(status_code=404, detail="Image not found")
            FILEPATH = "static/lawyers/"
            os.remove("static/lawyers/"+user.image)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
    filename = file.filename
    extention = filename.split(".")
    extention = extention[-1]
    if extention not in ["jpeg", "png","jpg","gif"]:
        raise HTTPException(status_code=400, detail="Unsupported file")
    token_name = secrets.token_hex(16) + "."+ extention
    generated_name = FILEPATH + token_name
    file_content = await file.read()
    with open(generated_name, "wb+") as file:
        file.write(file_content)
    #resize the picture:
    img = Image.open(generated_name)
    img = img.resize(size = (200,200))
    img.save(generated_name)
    file.close()
    user.image = token_name
    db.commit()
    db.refresh(user)
    return {"filename": token_name}  

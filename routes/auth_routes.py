from fastapi import APIRouter, Depends, HTTPException , Response 
from sqlalchemy.orm import Session
import bcrypt
from datetime import datetime
from database import get_db 
from models import *
from controllers import *
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
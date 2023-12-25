from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers.user_controller import *
from database import SessionLocal  
from models.user import *

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

user_route = APIRouter() 
@user_route.get("/users")
async def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(UserModel).offset(skip).limit(limit).all()
    return users


    
@user_route.post('/users/create_account')
async def create_user_account_route(user_data :UserCreate , db: Session = Depends(get_db)):
    existing_user =  db.query(UserModel).filter(UserModel.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="account already exicte log in please")
    user =  create_user_account(db, user_data = user_data)
    return {"message": "user created succesfully",
            "user": user}

@user_route.get('/users/get_par_email')
async def get_user_account(email : str , db: Session = Depends(get_db)):
    existing_user=  get_user_by_email(db , email = email)
    if(existing_user):
        return {"message ": "account found",
        "user" : existing_user}
    else:
        return {"message ": "account not found"}
@user_route.put("/users/{user_id}/update")
def update_user_account(
    user_id: int,
    user_data : UserUpdate,
    db: Session = Depends(get_db)
    ):
    existing_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not existing_user:
        return {"message":"user account not found"}
    updated_user =update_user(
        db,
        user_id,
        user_data
        )
    
    return {"message": "account updated succesfully",
    "updated account" : updated_user}


@user_route.delete("/users/{user_id}/delete")
def delete_user_account(user_id: int, db: Session = Depends(get_db)):
    existing_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not existing_user:
        return {"message":"user account not found"}
    deleted_user = delete_user(db, user_id)
    return {"message": "account deleted succesfully"}

@user_route.post("/users/login")
def login_user(email:str,password:str , db:Session = Depends(get_db)):
    return None
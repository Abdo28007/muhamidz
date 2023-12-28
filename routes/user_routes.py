from fastapi import APIRouter, Depends, HTTPException , Response 
from sqlalchemy.orm import Session
import bcrypt
from datetime import datetime


from database import get_db 
from models import *
from controllers import *

        


user_route = APIRouter() 
@user_route.get("/users")
async def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(UserModel).offset(skip).limit(limit).all()
    return users


    
@user_route.post('/create_account')
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




@user_route.put("/{user_id}/update")
def update_user_account(
    user_id: int,
    user_data : UserCreate ,
    #current_user : UserCreate = Depends(get_current_user),
    db: Session = Depends(get_db)
    ):
    #if user_id != current_user.id:
   #     raise HTTPException(status_code=400,detail="Not authorized to perform this action")
    existing_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    updated_user =update_user(
        db,
        user_id,
        user_data
        )
    
    return {"message": "account updated succesfully",
    "updated account" : updated_user}





@user_route.delete("/{user_id}/delete")
def delete_user_account(user_id: int, 
    db: Session = Depends(get_db)
    #current_user : UserCreate = Depends(get_current_user)
    ):
    #if user_id != current_user.id:
        #raise HTTPException(status_code=400,detail="Not authorized to perform this action")
    existing_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not existing_user:
        return {"message":"user account not found"}
    deleted_user = delete_user(db, user_id)
    return {"message": "account deleted succesfully"}




@user_route.post("/user-login")
async def login_for_access_token(user_info: LoginData  , db : Session = Depends(get_db)):
    # Authenticate the user against the database
    access_token = await authenticate_user(user_info.email,user_info.password,db)
    #response = Response()
    #response.set_cookie(key="access_token", value=access_token, httponly=True)
    return {"acces token " : access_token }



@user_route.post("/lawyer/{lawyer_id}/rate/{user_id}")
def user_rate_lawyer(
    user_id:int,
    lawyer_id :int,
    evaluation : EvaluationCreate,
    db : Session = Depends(get_db)
    ):
    #check if user and lawyer does not existe (stupid i know ) before adding authorization to this route
    user = db.query(UserModel).filter(UserModel.id==user_id).first()
    lawyer = db.query(LawyerModel).filter(LawyerModel.id==lawyer_id).first()
    if not  (lawyer or user):
        raise HTTPException(
            status_code = 404,
            detail = "error user or lawyer does not existe" 
        )
    rate = user_rate(db=db,user_id =user_id , lawyer_id=lawyer_id,commentaire = evaluation.commentaire,rating = evaluation.rating)
    
    total = get_lawyer_rating(db, lawyer_id)
    lawyer.rating = total
    db.commit()
    db.refresh(lawyer)
    return {
        "message " : "rating added succesfully",
        "rating": rate,
        "lawyer":lawyer
    }








@user_route.post("/{user_id}/upload/image")
async def create_upload_file(user_id: int, image: ImageCreate, file: UploadFile = File(...)):

    # Get the contents of the uploaded file
    file_content = file.file.read()

    # Create a new image entry in the database and associate it with the user
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()
    
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_image = Image(**image.dict(), data=file_content, user=db_user)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    db.close()

    return {"filename": file.filename, "user_id": user_id}
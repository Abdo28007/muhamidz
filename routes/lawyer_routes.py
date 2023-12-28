from fastapi import APIRouter, Depends, HTTPException , Response
from sqlalchemy.orm import Session
from controllers.lawyer_controller import *
from controllers.auth_controller import *
from database import SessionLocal  
from  models import *
lawyer_route = APIRouter() 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@lawyer_route.get("/lawyers")
async def get_lawyers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    lawyers = db.query(LawyerModel).offset(skip).limit(limit).all()
    return lawyers





@lawyer_route.post('/lawyers/create_account')
async def create_lawyer_account_route(
    lawyer_data : LawyerCreate,
    db: Session = Depends(get_db)
):
    existing_lawyer =  db.query(LawyerModel).filter(LawyerModel.email == lawyer_data.email).first()
    if existing_lawyer:
        raise HTTPException(status_code=400, detail="account already exicte ,log in please")
    lawyer_account =  create_lawyer_account(
        db,
        lawyer_data
    )
    return {"message": "lawyer account created succesfully , please log nigga",
            "lawyer_account": lawyer_account}





@lawyer_route.get("/lawyers/get_by_email")
async def get_lawyer_par_email(email : str,db: Session = Depends(get_db)):
    exicting_lawyer = get_lawyer_by_email(db,email=email)
    if(exicting_lawyer):
        return {'message': "amchi t3ti ",
        "lawyer" : exicting_lawyer}
    else:
        return{"message":"amchi 9wd mkach wach t7ws"}





@lawyer_route.put("/lawyers/{lawyer_id}/update")
def update_lawyer_account(
    lawyer_id: int,
    lawyer_data : LawyerCreate ,
    db: Session = Depends(get_db)
    ):
    existing_lawyer = db.query(LawyerModel).filter(LawyerModel.id == lawyer_id).first()
    if not existing_lawyer:
        return {"message":"Lawyer not found"}
    updated_lawyer =update_lawyer(
        db = db,
        lawyer_id = lawyer_id,
        lawyer_data  = lawyer_data   
    )
    
    return {"message": "account updated succesfully",
    "new account" : updated_lawyer}




@lawyer_route.delete("/lawyers/{lawyer_id}/delete")
def delete_lawyer_account(lawyer_id: int, db: Session = Depends(get_db)):
    existing_lawyer = db.query(LawyerModel).filter(LawyerModel.id == lawyer_id).first()
    if not existing_lawyer:
        return {"message":"Lawyer not found"}
    deleted_lawyer = delete_lawyer(db, lawyer_id)
    return {"message": "account deleted succesfully"}







@lawyer_route.get("/lawyer/{lawyer_id}/profile")
async def get_lawyer_profile(lawyer_id :int ,db :Session = Depends(get_db)):
    lawyer = db.query(LawyerModel).filter(LawyerModel.id == lawyer_id).first()
    if not lawyer:
        raise HTTPException(
            status_code=404, detail="Lawyer with this id does not exist."
        )
    commentaires = get_all_avis_for_lawyer(lawyer_id = lawyer_id, db=db)

    return {
        "user" : lawyer,
        "comments" : commentaires
    }


@lawyer_route.post("/lawyers/login")
async def login_for_access_token(user_info: LoginData  , db : Session = Depends(get_db)):
    access_token = await authenticate_lawyer(user_info.email,user_info.password,db)
    #response = Response()
    #response.set_cookie(key="access_token", value=access_token, httponly=True)
    return {"access token " : access_token }
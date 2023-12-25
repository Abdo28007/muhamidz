from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers.lawyer_controller import create_lawyer_account , get_lawyer_by_email, update_lawyer
from database import SessionLocal  
from models.lawyer import LawyerModel

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

lawyer_route = APIRouter() 
@lawyer_route.get("/lawyers")
async def get_users(db: Session = Depends(get_db)):
    users = get_users(db)
    return users

@lawyer_route.post('/lawyers/create_account')
async def create_lawyer_account_route(
    fullname: str,
    email: str,
    languages: str,
    gendre: str,
    phone_number: str,
    address: str,
    city: str,
    description: str,
    password:str,
    db: Session = Depends(get_db)
):
    existing_lawyer =  db.query(LawyerModel).filter(LawyerModel.email == email).first()
    if existing_lawyer:
        raise HTTPException(status_code=400, detail="account already exicte ,log in please")
    lawyer_account =  create_lawyer_account(
        db,
        fullname= fullname,
        email=email ,
        languages=languages ,
        gendre= gendre,
        phone_number= phone_number,
        address= address,
        city= city,
        description= description,
        password = password
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
    fullname: str,
    email: str,
    languages: str,
    gendre: str,
    phone_number: str,
    address: str,
    city: str,
    description: str,
    db: Session = Depends(get_db)
    ):
    existing_lawyer = db.query(LawyerModel).filter(LawyerModel.id == lawyer_id).first()
    if not existing_lawyer:
        return {"message":"Lawyer not found"}
    updated_lawyer =update_lawyer(
        db=db,
        lawyer_id=lawyer_id,
        fullname=fullname,
        email=email,
        languages=languages,
        gendre=gendre,
        phone_number=phone_number,
        address=address,
        city=city,
        description=description
        
    )
    
    return {"message": "account updated succesfully",
    "new account" : updated_lawyer}
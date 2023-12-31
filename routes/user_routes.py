from fastapi import APIRouter, Depends, HTTPException , Response 
from sqlalchemy.orm import Session
import bcrypt
from datetime import datetime
from database import get_db 
from models import *
from controllers import *
from dotenv import   dotenv_values
config = dotenv_values('.env')
user_route = APIRouter() 





@user_route.get("/users")
async def get_all_users( db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    return users


    
@user_route.post('/create_account')
async def create_user_account_route(user_data :UserCreate , db: Session = Depends(get_db)):
    existing_user =  db.query(UserModel).filter(UserModel.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="account already exicte log in please")
    if not existing_user:
        lawyer = db.query(LawyerModel).filter(LawyerModel.email == user_data.email).first()
        if lawyer:
            raise HTTPException(status_code=400, detail="account already exicte log in please")
        user =  await create_user_account(db, user_data = user_data)
    
    return {"message": "user created succesfully ",
            "user": user}




@user_route.put("/{user_id}/update")
async def update_user_account(user_id: int,user_data : UserCreate ,db: Session = Depends(get_db)):
    existing_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    updated_user =await update_user(db,user_id,user_data)
    return {"message": "account updated succesfully",
    "updated account" : updated_user}





@user_route.delete("/{user_id}/delete")
async def delete_user_account(user_id: int, db: Session = Depends(get_db)):
    existing_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not existing_user:
        return {"message":"user account not found"}
    deleted_user =await  delete_user(db, user_id)
    return {"message": "account deleted succesfully"}





@user_route.post("/lawyer/{lawyer_id}/rate/{user_id}")
async def user_rate_lawyer(user_id:int,lawyer_id :int,evaluation : EvaluationCreate,db : Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id==user_id).first()
    lawyer = db.query(LawyerModel).filter(LawyerModel.id==lawyer_id).first()
    avis = db.query(EvaluationModel).filter(EvaluationModel.user_id==user_id).all()
    if avis:
        for avi in avis:
            if avi.lawyer_id == lawyer_id:
                raise HTTPException(
                    status_code = 404,
                    detail = "error user already rate this lawyer" 
                    )
    if not  lawyer or  not user:
        raise HTTPException(
            status_code = 404,
            detail = "error user or lawyer does not existe" 
        )
    rate =await user_rate(db=db,user_id =user_id , lawyer_id=lawyer_id,commentaire = evaluation.commentaire,rating = evaluation.rating)
    total = await get_lawyer_rating(db, lawyer_id)
    lawyer.rating = total
    db.commit()
    db.refresh(lawyer)
    return {
        "message " : "rating added succesfully",
        "rating": rate,
        "lawyer":lawyer
    }






@user_route.delete("/user/{appoinement_id}/delete")
async def delete_rate(appoinement_id : int , db : Session = Depends(get_db)):
    rate = db.query(EvaluationModel).filter(EvaluationModel.id == appoinement_id).first()
    if not rate:
        raise HTTPException(status_code=404, detail="Rate not found")
    
    db.delete(rate)
    db.commit()
    total =   await get_lawyer_rating(db, rate.lawyer_id)
    lawyer = db.query(LawyerModel).filter(LawyerModel.id==rate.lawyer_id).first()
    lawyer.rating = total
    db.commit()
    db.refresh(lawyer)
    return {
        "message" : "rate deleted succesfully",
        "lawyer" :lawyer
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




@user_route.get("/search")
async def search( key : str , filter : str = "full name",db : Session= Depends(get_db)):
    if filter.lower() == "full name":
        lawyers = db.query(LawyerModel).filter(LawyerModel.fullname.ilike(f"%{key}%")).all()
    elif filter.lower() == "city":
        lawyers = db.query(LawyerModel).filter(LawyerModel.city.ilike(f"%{key}%")).all()
    elif filter.lower() == "category": 
        categorie_id = db.query(CategorieModel).filter(CategorieModel.categorie_name == key).first()
        lawyers_id = db.query(CategorieLawyer).filter.filter(CategorieLawyer.category_id).all()
        lawyers = {}
        for user in lawyers_id:
            lawyer = db.query(LawyerModel).filter(LawyerModel.id == user.Lawyer_id).first()
            lawyers.append(lawyer)
    elif filter.lower() == "phone number":
        lawyers = db.query(LawyerModel).filter(LawyerModel.phone_number.ilike(f"%{key}%")).all()
    elif filter.lower() == "email" :
        lawyers = db.query(LawyerModel).filter(LawyerModel.email.ilike(f"%{key}%")).all()
    return lawyers
    
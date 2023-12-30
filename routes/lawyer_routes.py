from fastapi import APIRouter, Depends, HTTPException , Response
from sqlalchemy.orm import Session
from controllers.lawyer_controller import *
from controllers.auth_controller import *
from database import SessionLocal  
from  models import *



lawyer_route = APIRouter() 
from jose import JWTError , jwt
from dotenv import   dotenv_values
config = dotenv_values('.env')
from datetime import datetime , timedelta , timezone


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@lawyer_route.get("/lawyers")
async def get_all_lawyers( db: Session = Depends(get_db)):
    lawyers = db.query(LawyerModel).all()
    return lawyers





@lawyer_route.post('/lawyers/create_account')
async def create_lawyer_account_route(
    lawyer_data : LawyerCreate,
    db: Session = Depends(get_db)):
    existing_lawyer =  db.query(LawyerModel).filter(LawyerModel.email == lawyer_data.email).first()
    if existing_lawyer:
        raise HTTPException(status_code=400, detail="account already exicte ,log in please")
    lawyer_account =  create_lawyer_account(
        db,
        lawyer_data
    )
    send_email = await send_lawyer_email_verification(db = db ,lawyer_id =lawyer_account.id)
    return {"message": "lawyer account created succesfully , verify ur email ",
            "lawyer_account": lawyer_account}






@lawyer_route.put("/{lawyer_id}/verify-email/{token}")
async def verify_lawyer(lawyer_id : int, token :str , db : Session = Depends(get_db)):
    lawyer =  db.query(LawyerModel).filter(LawyerModel.id == lawyer_id).first()
    if not lawyer:
        raise HTTPException(
            status_code = 404,
            detail = "User Not Found"
        )
   
    decoded_token = jwt.decode(token, config['SECRET_KEY'], algorithms=["HS256"])
    exp_timestamp = decoded_token['expired_in']
    exp_datetime = datetime.fromtimestamp(exp_timestamp, timezone.utc)
    if exp_datetime.timestamp() < exp_timestamp :
        raise HTTPException(
            status_code = 422,
            detail = "Token has Expired"
        )
    lawyer.is_activated = True
    db.commit()
    db.refresh(lawyer)

    return lawyer




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

<<<<<<< HEAD
=======

@lawyer_route.post("/lawyers/login")
async def login_for_access_token(user_info: LoginData  , db : Session = Depends(get_db)):
    access_token = await authenticate_lawyer(user_info.email,user_info.password,db)
    #response = Response()
    #response.set_cookie(key="access_token", value=access_token, httponly=True)
    return {"access token " : access_token }


@lawyer_route.get("/lawyers/search_by_name")
async def search_lawyer_by_name_route(query: str, db: Session = Depends(get_db)):
    lawyers = search_lawyer_by_name(db, query)
    return {"lawyers": lawyers}

@lawyer_route.get("/lawyers/search_by_category")
async def search_lawyer_by_category_route(category: str, db: Session = Depends(get_db)):
    lawyers = search_lawyer_by_category(db, category)
    return {"lawyers": lawyers}

@lawyer_route.get("/lawyers/search_by_city")
async def search_lawyer_by_city_route(city: str, db: Session = Depends(get_db)):
    lawyers = search_lawyer_by_city(db, city)
    return {"lawyers": lawyers}

@lawyer_route.get("/lawyers/search_by_phone_number")
async def search_lawyer_by_phone_number_route(phone_num: str, db: Session = Depends(get_db)):
    lawyers = search_lawyer_by_phone_number(db, phone_num)
    return {"lawyers": lawyers}

@lawyer_route.get("/lawyers/search_by_email")
async def search_lawyer_by_email_route(email: str, db: Session = Depends(get_db)):
    lawyers = search_lawyer_by_email(db, email)
    return {"lawyers": lawyers}
>>>>>>> appoint-sys

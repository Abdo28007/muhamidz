import bcrypt
from sqlalchemy.orm import Session
from models import *
from controllers import *
from fastapi import Depends
from datetime import datetime , timedelta
from jose import JWTError , jwt
from fastapi.responses import JSONResponse
from fastapi_mail import ConnectionConfig , FastMail , MessageSchema ,MessageType
from dotenv import   dotenv_values
config = dotenv_values('.env')
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
import secrets
from typing import Optional

async def generate_unique_id():
    return f"{secrets.randbelow(10**8):08d}"



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



LawyerCreateResponse = sqlalchemy_to_pydantic(LawyerModel, exclude=['id','password'])


async def create_lawyer_account( db: Session,lawyer_data: LawyerCreate) :
    # Check if the provided email is already in use
    existing_lawyer = db.query(LawyerModel).filter(LawyerModel.email == lawyer_data.email).first()
    if existing_lawyer:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password
    hashed_password =  hash_password(lawyer_data.password)
    _id = await  generate_unique_id()
    # Create a new lawyer instance
    new_lawyer = LawyerModel(
        id = _id,
        fullname=lawyer_data.fullname,
        email=lawyer_data.email,
        languages=lawyer_data.languages,
        gendre=lawyer_data.gendre,
        phone_number=lawyer_data.phone_number,
        address=lawyer_data.address,
        city=lawyer_data.city,
        description=lawyer_data.description,
        password=hashed_password
    )
    db.add(new_lawyer)
    db.commit()
    db.refresh(new_lawyer)
    lawyer_id = new_lawyer.id
    # Associate categories with the new lawyer
    for category_name in lawyer_data.categories:
        # Check if the category already exists
        category = db.query(CategorieModel).filter(CategorieModel.caegorie_name == category_name).first()

        # If the category doesn't exist, create and add it
        if not category:
            category = CategorieModel(caegorie_name=category_name)
            db.add(category)
            db.commit()
            db.refresh(category)
        # Associate the category with the new lawyer using the retrieved lawyer_id
        lawyer_category = CategorieLawyer(Lawyer_id=lawyer_id, category_id=category.id)
        db.add(lawyer_category)
        db.commit()
        db.refresh(category)
    return new_lawyer



async def send_lawyer_email_verification(db : Session, lawyer_id : int):
    expiration_time = datetime.utcnow() + timedelta(minutes=5)
    lawyer =  db.query(LawyerModel).filter(LawyerModel.id == lawyer_id).first()
    lawyer_email = lawyer.email
    expiration_time = datetime.utcnow() + timedelta(minutes=2)
    token =  jwt.encode(
        {
         "lawyer_id" : lawyer.id,
         "expired_in": expiration_time.timestamp()},
        config['SECRET_KEY'],
        algorithm=config['ALGORITHM'],
    )
    link = f"http://localhost:8000/{lawyer_id}/verify-email/{token}"
    html = f"""
            <p>Click here to verify your account </p>
            <center>
                <a href="{link}">
                    <button style="background-color: blue; color: white; padding: 10px 20px; border-radius: 5px; font-size: 16px;">Click Here</button>
                </a>
            </center>
        """


    message = MessageSchema(
            subject="Fastapi-Mail module",
            recipients=[lawyer.email],
            body=html,
            subtype=MessageType.html
            )
    
    mail =  FastMail(conf)
    try:
        await mail.send_message(message)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")






async def send_user_email_notification(db : Session,status : bool,lawyer_fullname : str,user_email : str,appoinement_refuse : Optional[RefuseAppoinement] = None,address :Optional[str] = None,time : Optional[datetime]=None ):
    if  not status:
        html = f"""
            <center>
                <p>your reservation has been refused with the lawyer {lawyer_fullname}  because of {appoinement_refuse.reason}  please choose anothe time   </p>
            </center>
            """
    else :
        html = f"""
            <center>
                <p>your reservation has been accepted with the lawyer {lawyer_fullname}  in {address} at {time} please dont be late  </p>
            </center>
            """


    message = MessageSchema(
            subject="MUHAMI_DZ",
            recipients=[user_email],
            body=html,
            subtype=MessageType.html
            )
    
    mail =  FastMail(conf)
    try:
        await mail.send_message(message)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")




def update_lawyer(db: Session, lawyer_id : int,lawyer_data : LawyerUpdate):
    existing_lawyer = db.query(LawyerModel).filter(LawyerModel.id == lawyer_id).first()
    existing_lawyer.fullname =  lawyer_data.fullname
    existing_lawyer.languages = lawyer_data.languages
    existing_lawyer.gendre = lawyer_data.gendre
    existing_lawyer.phone_number = lawyer_data.phone_number
    existing_lawyer.address = lawyer_data.address
    existing_lawyer.city = lawyer_data.city
    existing_lawyer.description = lawyer_data.description
    existing_lawyer.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(existing_lawyer)
    return existing_lawyer




async def delete_lawyer(db: Session,lawyer_id: int):
    existing_lawyer = db.query(LawyerModel).filter(LawyerModel.id == lawyer_id).first()
    db.delete(existing_lawyer)
    db.commit()
    return existing_lawyer




async def get_lawyer_rating(db :Session,lawyer_id :int ):
    lawyerrating = db.query(EvaluationModel).filter(EvaluationModel.lawyer_id== lawyer_id).all()
    if not lawyerrating:
        raise HTTPException(
            status_code = 500,
            detail = "no rating"
        )
    total = 0
    counter = 0
    for evaluation in lawyerrating:
        total += evaluation.rating
        counter += 1
    total = total/counter
    return total







def get_all_avis_for_lawyer(db : Session,lawyer_id):
    avis = db.query(EvaluationModel).filter(EvaluationModel.lawyer_id==lawyer_id).all()
    result = []
    for avi in avis:
        data={}
        user = db.query(UserModel).filter(UserModel.id==avi.user_id).first()
        data["user"] = user.fullname
        data['rating'] = avi.rating
        data['commentaire'] = avi.commentaire
        result.append(data)
    return result


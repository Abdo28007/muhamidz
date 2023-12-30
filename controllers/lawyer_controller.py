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



<<<<<<< HEAD
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

def create_lawyer_account(
    db: Session,
    lawyer_data : LawyerCreate):
    # Create a new lawyer instance
=======




LawyerCreateResponse = sqlalchemy_to_pydantic(LawyerModel, exclude=['id','password'])


def create_lawyer_account(
    db: Session,
    lawyer_data: LawyerCreate
) -> LawyerCreateResponse:
    # Check if the provided email is already in use
    existing_lawyer = db.query(LawyerModel).filter(LawyerModel.email == lawyer_data.email).first()
    if existing_lawyer:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password
>>>>>>> appoint-sys
    hashed_password = hash_password(lawyer_data.password)

    # Create a new lawyer instance
    new_lawyer = LawyerModel(
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

    # Add the new lawyer to the database
    db.add(new_lawyer)
    db.commit()
    db.refresh(new_lawyer)
<<<<<<< HEAD
    return new_lawyer
=======

    # Now retrieve the lawyer's ID after it has been committed
    lawyer_id = new_lawyer.id
    print("HEHEH"+str(lawyer_id))


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

    return LawyerCreateResponse.from_orm(new_lawyer)
>>>>>>> appoint-sys



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

<<<<<<< HEAD
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
=======



def send_email_verification():
    pass

>>>>>>> appoint-sys


 


def update_lawyer(
    db: Session,
    lawyer_id : int,
    lawyer_data : LawyerCreate = Depends(get_current_user)) :
    existing_lawyer = db.query(LawyerModel).filter(LawyerModel.id == lawyer_id).first()
    if lawyer_data.id != lawyer_id:
        raise HTTPException(status_code=404, detail="Unotherized")
    existing_lawyer.fullname =  lawyer_data.fullname
    existing_lawyer.email = lawyer_data.email
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




def delete_lawyer(db: Session,lawyer_id: int,lawyer_data : LawyerCreate = Depends(get_current_user) ):
    existing_lawyer = db.query(LawyerModel).filter(LawyerModel.id == lawyer_id).first()
    if lawyer_data.id != lawyer_id:
        raise HTTPException(status_code=404, detail="Unotherized")
    db.delete(existing_lawyer)
    db.commit()
    return existing_lawyer




def get_lawyer_rating(db :Session,lawyer_id :int ):
    lawyerrating = db.query(EvaluationModel).filter(EvaluationModel.lawyer_id== lawyer_id).all()
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
        user = get_user_by_id(db ,avi.user_id)
        data["user"] = user.fullname
        data['rating'] = avi.rating
        data['commentaire'] = avi.commentaire
        result.append(data)
    return result


def search_lawyer_by_name(db: Session, query: str):
    return db.query(LawyerModel).filter(LawyerModel.fullname.ilike(f"%{query}%")).all()

def search_lawyer_by_category(db: Session, category: str):
    return db.query(LawyerModel).filter(LawyerModel.categories.any(CategorieModel.name.ilike(f"%{category}%"))).all()

def search_lawyer_by_city(db: Session, city: str):
    return db.query(LawyerModel).filter(LawyerModel.city.ilike(f"%{city}%")).all()

def search_lawyer_by_phone_number(db: Session, phone_num: str):
    return db.query(LawyerModel).filter(LawyerModel.phone_number.ilike(f"%{phone_num}%")).all()

def search_lawyer_by_email(db: Session, email: str):
    return db.query(LawyerModel).filter(LawyerModel.email.ilike(f"%{email}%")).all()

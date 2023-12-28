import bcrypt
from sqlalchemy.orm import Session
from models import *
from controllers import *
from fastapi import Depends
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from datetime import datetime , timedelta
from jose import JWTError , jwt
from fastapi.responses import JSONResponse







LawyerCreateResponse = sqlalchemy_to_pydantic(LawyerModel, exclude=['id','password'])





def create_lawyer_account(
    db: Session,
    lawyer_data : LawyerCreate
) -> LawyerCreateResponse:
    # Create a new lawyer instance
    hashed_password = hash_password(lawyer_data.password)
    new_lawyer = LawyerModel(
        fullname=lawyer_data.fullname,
        email=lawyer_data.email,
        languages=lawyer_data.languages,
        gendre=lawyer_data.gendre,
        phone_number=lawyer_data.phone_number,
        address=lawyer_data.address,
        city=lawyer_data.city,
        description=lawyer_data.description,
        password = hashed_password
    )

    # Add the new lawyer to the database
    db.add(new_lawyer)
    db.commit()
    db.refresh(new_lawyer)

    return LawyerCreateResponse.from_orm(new_lawyer)




def send_email_verification():
    pass



 
def get_lawyer_by_email(db: Session, email: str) -> LawyerCreateResponse:
    lawyer = db.query(LawyerModel).filter(LawyerModel.email == email).first()
    return LawyerCreateResponse.from_orm(lawyer) if lawyer else None




def det_lawyers (db :Session):
    lawyerrs = db.query(LawyerModel).all()
    return JSONResponse(content =lawyers)




def update_lawyer(
    db: Session,
    lawyer_id : int,
    lawyer_data : LawyerCreate = Depends(get_current_lawyer)
) -> LawyerCreateResponse:
    # Check if the lawyer with the specified ID exists
    existing_lawyer = db.query(LawyerModel).filter(LawyerModel.id == lawyer_id).first()
    if existing_lawyer.id != lawyer_id:
        raise HTTPException(status_code=404, detail="Unotherized")
    # Update the lawyer's information
    existing_lawyer.fullname =  lawyer_data.fullname
    existing_lawyer.email = lawyer_data.email
    existing_lawyer.languages = lawyer_data.languages
    existing_lawyer.gendre = lawyer_data.gendre
    existing_lawyer.phone_number = lawyer_data.phone_number
    existing_lawyer.address = lawyer_data.address
    existing_lawyer.city = lawyer_data.city
    existing_lawyer.description = lawyer_data.description
    existing_lawyer.updated_at = datetime.utcnow()

    # Commit the changes to the database
    db.commit()
    db.refresh(existing_lawyer)

    return LawyerCreateResponse.from_orm(existing_lawyer)




def delete_lawyer(db: Session, lawyer_id: int):
    # Check if the user with the specified ID exists
    existing_lawyer = db.query(LawyerModel).filter(LawyerModel.id == lawyer_id).first()
    # Delete the user from the database
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
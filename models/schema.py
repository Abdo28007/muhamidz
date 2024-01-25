from pydantic import BaseModel , EmailStr 
from typing import List, Optional
from datetime import datetime
from typing import List

class UserCreate(BaseModel):
    fullname: str 
    email: EmailStr
    password: str

class LoginData(BaseModel):
    email : EmailStr
    password :str

class ImageCreate(BaseModel):
    filename : str

class resetPassword(BaseModel):
    old_password : str
    new_password : str

class LawyerCreate(BaseModel):
    fullname: str
    email: EmailStr
    languages: str
    gendre: str
    phone_number: str
    address: str
    city: str
    description: str
    password : str
    class Config:
        orm_mode = True
        from_orm = True
    categories: List[str]

class LawyerUpdate(BaseModel):
    fullname: str
    languages: str
    gendre: str
    phone_number: str
    address: str
    city: str
    description: str
    categories: List[str]
    class Config:
        orm_mode = True
        from_orm = True

class EvaluationCreate(BaseModel):
    commentaire: str
    rating: int

class EmailSchema(BaseModel):
    email: List[EmailStr]

class PasswordSchema(BaseModel):
    password : str

class AppointmentRequest(BaseModel):
    description : str
    appointment_time: datetime

class RefuseAppoinement(BaseModel):
    reason : str
class AppointmentResponse(BaseModel):
    message: str
    data: AppointmentRequest

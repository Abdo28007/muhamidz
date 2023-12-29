from pydantic import BaseModel , EmailStr 

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


class EvaluationCreate(BaseModel):
    commentaire: str
    rating: int

class EmailSchema(BaseModel):
    email: List[EmailStr]
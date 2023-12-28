from pydantic import BaseModel , EmailStr

from datetime import datetime


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


class EvaluationCreate(BaseModel):
    commentaire: str
    rating: int


# main.py

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import database, SessionLocal
from models import User

app = FastAPI()

@app.on_event("startup")
async def startup_db():
    await database.connect()
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown_db():
    await database.disconnect()

# Your FastAPI routes and other logic go here

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}
@app.post("/create_user")
async def create_user(user: User):
    async with database.transaction():
        db_user = User(**user.dict())
        database.execute(User.__table__.insert().values(db_user))
    return {"user": user.dict(), "message": "User created successfully"}

@app.get("/users/me", response_model=User)
async def read_current_user():
    """
    Get information about the current user.
    """
    return {"message": "User information retrieved successfully"}
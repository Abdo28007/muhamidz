from fastapi import FastAPI 
from routes import user_route as user_routes
from routes import lawyer_route as lawyer_routes
from routes.time_availability_routes import time_availability_route as time_availability_routes
from routes.appointments_routes import appointment_route as appointments_routes
from database import engine 
import models 
app = FastAPI()
app.include_router(user_routes)
app.include_router(lawyer_routes)
app.include_router(time_availability_routes)
app.include_router(appointments_routes)

models.Base.metadata.create_all(bind = engine)
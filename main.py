from fastapi import FastAPI 
from routes import user_route as user_routes
from routes import lawyer_route as lawyer_routes
from routes import time_availability_route as  time_availability_routes
from routes import appointment_route as appointments_routes
from routes import auth_route as auth_routes
app = FastAPI()
app.include_router(user_routes)
app.include_router(lawyer_routes)
app.include_router(time_availability_routes)
app.include_router(appointments_routes)
app.include_router(auth_routes)
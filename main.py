from fastapi import FastAPI 
from routes import user_route as user_routes
from routes import lawyer_route as lawyer_routes
from routes import auth_route as auth_routes
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.include_router(user_routes)
app.include_router(lawyer_routes)
app.include_router(auth_routes)


app.add_middleware(SessionMiddleware, secret_key="add any string...")
app.mount("/static", StaticFiles(directory="statics"), name="static")
templates = Jinja2Templates(directory="templates")
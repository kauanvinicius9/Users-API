from fastapi import FastAPI
from app.routers import users

app = FastAPI(title="Users API")
app.include_router(users.router)
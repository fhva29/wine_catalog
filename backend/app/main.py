# app/main.py
from fastapi import FastAPI
from .database import Base, engine
from .routers import wines, moments

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(wines.router)
app.include_router(moments.router)

# app/main.py
from fastapi import FastAPI
from .database import Base, engine
from .routers import wines, moments
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou restrinja ao domínio do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(wines.router)
app.include_router(moments.router)

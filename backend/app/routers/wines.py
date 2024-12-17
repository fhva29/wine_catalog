from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/wines", response_model=list[schemas.Wine])
def list_wines(db: Session = Depends(get_db)):
    return crud.get_wines(db)


@router.post("/wines", response_model=schemas.Wine)
def create_new_wine(wine: schemas.WineCreate, db: Session = Depends(get_db)):
    return crud.create_wine(db, wine)


@router.get("/wines/{wine_id}", response_model=schemas.Wine)
def get_wine_detail(wine_id: int, db: Session = Depends(get_db)):
    wine = crud.get_wine(db, wine_id)
    if not wine:
        raise HTTPException(status_code=404, detail="Wine not found")
    return wine

# app/routers/moments.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database, models

router = APIRouter()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/wines/{wine_id}/moments", response_model=schemas.Moment)
def create_moment_for_wine(
    wine_id: int, moment: schemas.MomentCreate, db: Session = Depends(get_db)
):
    wine = crud.get_wine(db, wine_id)
    if not wine:
        raise HTTPException(status_code=404, detail="Wine not found")
    return crud.create_moment(db, wine_id, moment)

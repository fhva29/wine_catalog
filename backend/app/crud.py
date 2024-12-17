# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas


def get_wines(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Wine).offset(skip).limit(limit).all()


def create_wine(db: Session, wine: schemas.WineCreate):
    db_wine = models.Wine(**wine.model_dump())
    db.add(db_wine)
    db.commit()
    db.refresh(db_wine)
    return db_wine


def get_wine(db: Session, wine_id: int):
    return db.query(models.Wine).filter(models.Wine.id == wine_id).first()


def create_moment(db: Session, wine_id: int, moment: schemas.MomentCreate):
    db_moment = models.Moment(
        wine_id=wine_id, name=moment.name, description=moment.description
    )
    db.add(db_moment)
    db.commit()
    db.refresh(db_moment)

    # Criar as imagens do momento
    for image_url in moment.images:
        db_image = models.MomentImage(moment_id=db_moment.id, image_url=image_url)
        db.add(db_image)
    db.commit()
    db.refresh(db_moment)

    return db_moment

# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Wine(Base):
    __tablename__ = "wines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    grape = Column(String, nullable=True)
    description = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    moments = relationship("Moment", back_populates="wine")


class Moment(Base):
    __tablename__ = "moments"

    id = Column(Integer, primary_key=True, index=True)
    wine_id = Column(Integer, ForeignKey("wines.id"))
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    wine = relationship("Wine", back_populates="moments")
    images = relationship("MomentImage", back_populates="moment", cascade="all, delete")


class MomentImage(Base):
    __tablename__ = "moment_images"

    id = Column(Integer, primary_key=True, index=True)
    moment_id = Column(Integer, ForeignKey("moments.id"))
    image_url = Column(String, nullable=False)

    moment = relationship("Moment", back_populates="images")

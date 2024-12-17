# app/schemas.py
from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class MomentImage(BaseModel):
    id: int
    image_url: HttpUrl

    class Config:
        orm_mode = True


class MomentBase(BaseModel):
    name: str
    description: Optional[str]


class MomentCreate(MomentBase):
    images: List[HttpUrl] = []


class Moment(MomentBase):
    id: int
    images: List[MomentImage] = []

    class Config:
        orm_mode = True


class WineBase(BaseModel):
    name: str
    grape: Optional[str]
    description: Optional[str]
    image_url: Optional[HttpUrl]


class WineCreate(WineBase):
    pass


class Wine(WineBase):
    id: int
    moments: List[Moment] = []

    class Config:
        orm_mode = True

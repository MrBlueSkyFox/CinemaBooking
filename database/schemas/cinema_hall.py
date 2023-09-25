from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class CinemaHallBase(BaseModel):
    name: str
    rows: int
    places_per_row: int

    class Config:
        orm_mode = True


class CinemaHallId(BaseModel):
    id: UUID


class CinemaHall(CinemaHallBase, CinemaHallId):
    pass


class CinemaHallCreate(CinemaHallBase):
    pass


class CinemaHallUpdate(CinemaHallBase):
    name: Optional[str]
    rows: Optional[int]
    places_per_row: Optional[int]

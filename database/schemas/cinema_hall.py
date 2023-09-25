from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class CinemaHall(BaseModel):
    id: UUID
    name: str

    class Config:
        orm_mode = True


class CinemaHallCreate(CinemaHall):
    rows: int
    places_per_row: int


class CinemaHallUpdate(BaseModel):
    name: Optional[str]
    rows: Optional[int]
    places_per_row: Optional[int]

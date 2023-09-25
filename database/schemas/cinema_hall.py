from uuid import UUID

from pydantic import BaseModel


class CinemaHall(BaseModel):
    id: UUID
    name: str
    # rows: int
    # places_per_row: int

    class Config:
        orm_mode = True

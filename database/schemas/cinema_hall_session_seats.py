from uuid import UUID

from pydantic import BaseModel


class CinemaHallSessionSeats(BaseModel):
    session_id: UUID
    seats: list[list[int]]

    class Config:
        orm_mode = True

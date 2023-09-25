from uuid import UUID

from pydantic import BaseModel


class Seat(BaseModel):
    row: int
    place_in_row: int

    class Config:
        orm_mode = True

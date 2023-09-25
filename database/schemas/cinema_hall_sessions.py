import datetime
from typing import Annotated
from uuid import UUID
from pydantic import BaseModel, BeforeValidator
from .movie import force_image_uri


class CinemaHallSession(BaseModel):
    id: UUID
    hall_name: str
    movie_name: str
    session_start: datetime.datetime
    picture: Annotated[str, BeforeValidator(force_image_uri)]

    class Config:
        orm_mode = True

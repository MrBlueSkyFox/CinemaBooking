import base64
from typing import Optional, Annotated
from uuid import UUID

from fastapi import File
from pydantic import BaseModel, BeforeValidator


def force_image_uri(value: bytes) -> str:
    img_base64_encoded = base64.b64encode(value).decode('ascii')
    img_type = 'image/jpg'  # Use some smart image type guessing if applicable

    img_data_uri = f'data:{img_type};base64,{img_base64_encoded}'
    return img_data_uri


class MovieBase(BaseModel):
    name: Optional[str]
    picture: Annotated[str, BeforeValidator(force_image_uri)]

    class Config:
        orm_mode = True


class Movie(MovieBase):
    id: UUID


class MovieChange(MovieBase):
    picture: bytes


class MovieUpdate(MovieChange):
    picture: Optional[bytes]


class MovieCreate(MovieChange):
    pass

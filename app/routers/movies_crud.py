from uuid import UUID

from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK

import database.schemas as schemas
from database import DataBase

from ..dependencies import get_db

router = APIRouter(
    prefix="/movies",
    dependencies=[Depends(get_db)],
)


@router.get("/", response_model=list[schemas.Movie])
def get_all_movies(db: DataBase = Depends(get_db)):
    movies = db.get_all_movies()
    return movies


@router.get("/{movie_id}", response_model=schemas.Movie)
def get_movie_by_id(movie_id: UUID, db: DataBase = Depends(get_db)):
    movie = db.get_movie_by_id(movie_id)
    return movie


@router.post("/")
def create_movie(movie_create: schemas.MovieCreate, db: DataBase = Depends(get_db)):
    db.create_movie(movie_create)
    return {"status_code": HTTP_200_OK}


@router.patch("/{movie_id}")
def update_movie(movie_id: UUID, movie_update: schemas.MovieUpdate, db: DataBase = Depends(get_db)):
    db.update_move_by_id(movie_id, movie_update)
    return {"status_code": HTTP_200_OK}

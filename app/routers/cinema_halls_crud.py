from uuid import UUID

from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK

import database.schemas as schemas
from database import DataBase

from ..dependencies import get_db

router = APIRouter(
    prefix="/cinema_halls",
    dependencies=[Depends(get_db)],
)


@router.get("/", response_model=list[schemas.CinemaHall])
def get_all_cinema_halls(db: DataBase = Depends(get_db)):
    cinema_halls = db.get_all_cinema_halls()
    return cinema_halls


@router.get("/{cinema_hall_id}", response_model=schemas.CinemaHall)
def get_cinema_hall_by_id(cinema_hall_id: UUID, db: DataBase = Depends(get_db)):
    cinema_hall = db.get_cinema_hall_by_id(cinema_hall_id)
    return cinema_hall


@router.post("/")
def create_cinema_hall(cinema_hall_create: schemas.CinemaHallCreate, db: DataBase = Depends(get_db)):
    db.create_cinema_hall(cinema_hall_create)
    return {"status_code": HTTP_200_OK}


@router.patch("/{cinema_hall_id}")
def update_cinema_hall(cinema_hall_id: UUID,
                       cinema_hall_update: schemas.CinemaHallUpdate, db: DataBase = Depends(get_db)):
    db.update_cinema_hall_by_id(cinema_hall_id, cinema_hall_update)
    return {"status_code": HTTP_200_OK}


@router.delete("/{cinema_hall_id}")
def delete_movie(cinema_hall_id: UUID, db: DataBase = Depends(get_db)):
    db.delete_cinema_hall_by_id(cinema_hall_id)
    return {"status_code": HTTP_200_OK}

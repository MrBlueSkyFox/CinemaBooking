from uuid import UUID

from sqlalchemy import select, delete

import database.schemas as schemas
from .db_base import DataBaseBase
from .models import CinemaHall


class CinemaHallsCRUD(DataBaseBase):
    def get_all_cinema_halls(self) -> list[CinemaHall]:
        stmt = select(CinemaHall)
        cinema_halls = self._select_objects(stmt)
        return cinema_halls

    def get_cinema_hall_by_id(self, cinema_hall_id: UUID) -> CinemaHall:
        stmt = select(CinemaHall).where(CinemaHall.id == cinema_hall_id)
        cinema_hall = self._select_one_object(stmt)
        return cinema_hall

    def create_cinema_hall(self, cinema_hall_data: schemas.CinemaHallCreate):
        cinema_hall = CinemaHall(**cinema_hall_data.model_dump())
        self.add_object(cinema_hall)
        self.commit_changes()

    def update_cinema_hall_by_id(self, cinema_hall_id: UUID, cinema_hall_data: schemas.CinemaHallUpdate):
        cinema_hall = self.get_cinema_hall_by_id(cinema_hall_id)
        if cinema_hall.name:
            cinema_hall.name = cinema_hall_data.name
        if cinema_hall.rows:
            cinema_hall.rows = cinema_hall_data.rows
        if cinema_hall.places_per_row:
            cinema_hall.places_per_row = cinema_hall_data.places_per_row
        self.commit_changes()

    def delete_cinema_hall_by_id(self, cinema_hall_id: UUID):
        stmt = delete(CinemaHall).where(CinemaHall.id == cinema_hall_id)
        self._execute(stmt)

from typing import Optional, Any
from uuid import UUID

from sqlalchemy import create_engine, URL, select
from sqlalchemy.orm import Session, sessionmaker

from database.models import Base, Movie, CinemaHall, CinemaSessions, Ticket

database_2 = {
    'drivername': 'postgresql',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': '3ruzkc23',
    'database': 'CinemaBooking'
}
engine = create_engine(URL.create(**database_2))
SessionLocal: sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class DataBaseBase:

    def __init__(self):
        self.engine = engine
        self.session: Session = SessionLocal()

    def create_all(self):
        Base.metadata.create_all(self.engine)

    def get_unavailable_seats_movie_session(self, movie_session_id: UUID) -> list:
        stmt = select(
            CinemaSessions.id.label('cinema_session_id'),
            Ticket.row,
            Ticket.place_in_row
        ).join(Ticket.cinema_session). \
            select_from(CinemaSessions). \
            where(CinemaSessions.id == movie_session_id)
        cinema_seats_unavailable = self._select_rows_all(stmt)
        return cinema_seats_unavailable

    def get_cinema_hall_by_movie_session(self, cinema_session_id) -> CinemaHall:
        stmt = select(CinemaHall).join(CinemaSessions).where(CinemaSessions.id == cinema_session_id)
        cinema_hall = self._select_one_object(stmt)
        return cinema_hall

    def get_movie_sessions_by_hall_name(self, hall_name: str) -> list:
        stmt = select(
            CinemaHall.name.label('hall_name'),
            Movie.name.label('movie_name'),
            Movie.picture,
            CinemaSessions.session_start,
            CinemaSessions.id
        ).join(CinemaSessions,
               CinemaSessions.cinema_hall_id == CinemaHall.id
               ).join(Movie,
                      CinemaSessions.movie_id == Movie.id
                      ).where(CinemaHall.name == hall_name)
        res = self._select_rows_all(stmt)
        return res

    def get_movie_by_name(self, name_val: str) -> Movie:
        stmt = select(Movie).where(Movie.name == name_val)
        movie = self._select_one_object(stmt)
        return movie

    def get_cinema_session_by_id(self, cinema_session_id: UUID) -> CinemaSessions:
        stmt = select(CinemaSessions).where(CinemaSessions.id == cinema_session_id)
        cinema_session = self._select_one_object(stmt)
        return cinema_session

    def get_cinema_hall_by_name(self, name_val: str) -> CinemaHall:
        stmt = select(CinemaHall).where(CinemaHall.name == name_val)
        cinema_hall = self._select_one_object(stmt)
        return cinema_hall

    def add_multiply_objects(self, list_of_objects: list):
        self.session.add_all(list_of_objects)

    def add_object(self, object_orm):
        self.session.add(object_orm)

    def _select_objects(self, query_to_execute) -> Optional[Any]:
        res = self.session.scalars(query_to_execute).all()
        return res

    def _select_one_object(self, statement_to_execute) -> Optional[Any]:
        res = self.session.scalars(statement_to_execute).first()
        return res

    def _select_rows(self, query_to_execute) -> Optional[Any]:
        res = self.session.execute(query_to_execute)
        return res

    def _select_rows_all(self, query_to_execute) -> Optional[Any]:
        res = self.session.execute(query_to_execute).all()
        return res

    def _select_one_row(self, query_to_execute) -> Optional[Any]:
        res = self.session.execute(query_to_execute).first()
        return res

    def _execute(self, statement_to_execute) -> Optional[Any]:
        res = self.session.execute(statement_to_execute)
        return res

    def commit_changes(self):
        self.session.commit()

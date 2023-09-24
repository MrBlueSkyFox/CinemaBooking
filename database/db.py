from typing import Union, Optional, Any

from sqlalchemy import create_engine, URL, select, Engine
from sqlalchemy.orm import Session, sessionmaker

from database.models import Base, Movie, CinemaHall

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


class DataBase:

    def __init__(self):
        self.engine = engine
        self.session: Session = SessionLocal()

    def create_all(self):
        Base.metadata.create_all(self.engine)



    def get_movie_by_name(self, name_val: str) -> Movie:
        stmt = select(Movie).where(Movie.name == name_val)
        movie = self._select_one_object(stmt)
        return movie

    def get_cinema_hall_by_name(self, name_val: str) -> CinemaHall:
        stmt = select(CinemaHall).where(CinemaHall.name == name_val)
        cinema_hall = self._select_one_object(stmt)
        return cinema_hall

    def add_multiply_objects(self, list_of_objects: list):
        self.session.add_all(list_of_objects)

    def _select_objects(self, query_to_execute) -> Optional[Any]:
        res = self.session.scalars(query_to_execute).all()
        return res

    def _select_one_object(self, statement_to_execute) -> Optional[Any]:
        res = self.session.scalars(statement_to_execute).first()
        return res

    def _select_rows(self, query_to_execute) -> Optional[Any]:
        res = self.session.execute(query_to_execute)
        return res

    def _select_one_row(self, query_to_execute) -> Optional[Any]:
        res = self.session.execute(query_to_execute).first()
        return res

    def _execute(self, statement_to_execute) -> Optional[Any]:
        res = self.session.execute(statement_to_execute)
        return res

    def commit_changes(self):
        self.session.commit()

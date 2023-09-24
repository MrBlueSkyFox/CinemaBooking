from typing import Union, Optional, Any

from sqlalchemy import create_engine, URL, select
from sqlalchemy.orm import Session

from database.models import Base, Movie, CinemaHall


class DataBase:

    def __init__(self, host: str, port: [Union[str, int]], username: str,
                 password: str, database: str, drivername: str = 'postgresql',
                 echo_debug: bool = False):
        self.engine = create_engine(URL.create(
            drivername,
            username,
            password,
            host,
            port,
            database), echo=echo_debug)
        self.session: Session = Session(self.engine, autoflush=False)
        self._dbname = database
        self._user = username
        self._password = password
        self._host = host
        self._port = port

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

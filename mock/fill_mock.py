import datetime
from database import DataBase
from database.models import CinemaHall, Movie, CinemaSessions
from .mock_data import MOVIES_MOCK, CINEMA_SESSIONS, CINEMA_HALL_MOCK


class FillMock:
    def __init__(self, db: DataBase):
        self.db = db

    def fill_with_default_mock(self):
        self.add_cinema_hall_mock(CINEMA_HALL_MOCK)
        self.add_movies_mock(MOVIES_MOCK)
        self.add_cinema_sessions_mock(CINEMA_SESSIONS)

    def add_cinema_hall_mock(self, data):
        cinema_halls = self.create_cinema_hall_from_mock(data)
        self.db.add_multiply_objects(cinema_halls)
        self.db.commit_changes()

    def add_movies_mock(self, data):
        movies = self.create_movies_from_mock(data)
        self.db.add_multiply_objects(movies)
        self.db.commit_changes()

    def add_cinema_sessions_mock(self, data):

        cinema_sessions = self.create_cinema_sessions(data)
        self.db.add_multiply_objects(cinema_sessions)
        self.db.commit_changes()

    @staticmethod
    def create_cinema_hall_from_mock(cinema_halls_mock: list[tuple[str, int, int]]) -> \
            list[CinemaHall]:
        cinema_halls = []
        for mock in cinema_halls_mock:
            cinema_hall = CinemaHall(name=mock[0], rows=mock[1], places_per_row=mock[2])
            cinema_halls.append(cinema_hall)

        return cinema_halls

    @staticmethod
    def create_movies_from_mock(movies_mock: list[tuple[str, str]]) -> list[Movie]:
        movies = []
        for mock in movies_mock:
            with open(mock[1], "rb") as img_file:
                img_bin = img_file.read()
                movie = Movie(name=mock[0], picture=img_bin)
                movies.append(movie)
        return movies

    def create_cinema_sessions(self, cinema_sessions_mock: list[str, str, datetime.datetime]) \
            -> list[CinemaSessions]:
        cinema_sessions = []
        for mock in cinema_sessions_mock:
            movie = self.db.get_movie_by_name(mock[0])
            cinema_hall = self.db.get_cinema_hall_by_name(mock[1])
            cinema_session = CinemaSessions(movie_id=movie.id,
                                            cinema_hall_id=cinema_hall.id, session_start=mock[2])

            cinema_sessions.append(cinema_session)
        return cinema_sessions

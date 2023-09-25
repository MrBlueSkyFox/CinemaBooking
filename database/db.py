from .movie_crud import MovieCRUD
from .cinema_halls_crud import CinemaHallsCRUD


class DataBase(MovieCRUD, CinemaHallsCRUD):
    pass

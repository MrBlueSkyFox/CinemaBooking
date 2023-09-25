from uuid import UUID

from sqlalchemy import select, delete

import database.schemas as schemas
from .db_base import DataBaseBase
from .models import Movie


class MovieCRUD(DataBaseBase):
    def get_all_movies(self) -> list[Movie]:
        stmt = select(Movie)
        movies = self._select_objects(stmt)
        return movies

    def get_movie_by_id(self, movie_id: UUID) -> Movie:
        stmt = select(Movie).where(Movie.id == movie_id)
        movie = self._select_one_object(stmt)
        return movie

    def create_movie(self, movie_data: schemas.MovieCreate):
        movie = Movie(**movie_data.model_dump())
        self.add_object(movie)
        self.commit_changes()

    def update_move_by_id(self, movie_id: UUID, movie_data: schemas.MovieUpdate):
        movie = self.get_movie_by_id(movie_id)
        if movie_data.name:
            movie.name = movie_data.name
        if movie_data.picture:
            movie.picture = movie_data.picture
        self.commit_changes()

    def delete_movie_by_id(self, movie_id: UUID) -> None:
        movie = self.get_movie_by_id(movie_id)
        self.session.delete(movie)
        self.commit_changes()

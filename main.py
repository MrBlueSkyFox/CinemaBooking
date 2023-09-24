from sqlalchemy.orm import Session

from database import DataBase, engine
from mock import FillMock
from fastapi import FastAPI, Depends

app = FastAPI()


# Dependency
def get_db():
    db = DataBase()
    try:
        yield db
    finally:
        db.session.close()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/all_rooms")
def get_all_cinema_halls(db: Session = Depends(get_db)):
    # 1
    pass


@app.get("/movies_for_room/{room_name}")
def get_movies_session_in_room(room_name: str, db: Session = Depends(get_db)):
    # 2
    pass


@app.get("/seats_in_session/{room_name}")
def get_seats_movie_session(room_name: str, db: Session = Depends(get_db)):
    # 3
    pass


def fill_with_default_mock(db: DataBase):
    fill_mock = FillMock(db)
    fill_mock.fill_with_default_mock()


if __name__ == "__main__":
    pass

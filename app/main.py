from uuid import UUID

from starlette.responses import Response
from starlette.status import HTTP_200_OK
from fastapi import FastAPI, Depends

from database import DataBase
import database.schemas as schemas
from mock import FillMock

from .routers import movies_crud, cinema_halls_crud

from .dependencies import get_db
from .data_to_orm import create_ticket

app = FastAPI()

app.include_router(movies_crud.router)
app.include_router(cinema_halls_crud.router)


@app.get("/generate_mock")
def generate_mock_and_create_db(db: DataBase = Depends(get_db)):
    db.create_all()
    fill_with_default_mock(db)

    return {"Created"}


@app.get("/all_rooms", response_model=list[schemas.CinemaHall])
def get_all_cinema_halls(db: DataBase = Depends(get_db)):
    cinema_halls = db.get_all_cinema_halls()
    return cinema_halls


# Can be changed to UUID of room
@app.get("/movies_for_room/{room_name}", response_model=list[schemas.CinemaHallSession])
def get_movies_session_in_room(room_name: str, db: DataBase = Depends(get_db)):
    movie_sessions = db.get_movie_sessions_by_hall_name(room_name)
    return movie_sessions


@app.get("/seats_in_session/{cinema_session_id}", response_model=schemas.CinemaHallSessionSeats)
def get_seats_movie_session(cinema_session_id: UUID, db: DataBase = Depends(get_db)):
    unavailable_seats = db.get_unavailable_seats_movie_session(cinema_session_id)
    cinema_hall = db.get_cinema_hall_by_movie_session(cinema_session_id)
    rows, cols = cinema_hall.rows, cinema_hall.places_per_row
    cinema_seats = [
        [0 for i in range(cols)] for j in range(rows)
    ]
    for seat in unavailable_seats:
        cinema_seats[seat.row][seat.place_in_row] = 1
    return schemas.CinemaHallSessionSeats(session_id=cinema_session_id, seats=cinema_seats)


@app.post("/seats_in_session/{cinema_session_id}")
def create_purchase_tickets(cinema_session_id: UUID, selected_places: list[schemas.Seat],
                            db: DataBase = Depends(get_db)):
    # 3
    cinema_session = db.get_cinema_session_by_id(cinema_session_id)
    tickets = []
    for selected_place in selected_places:
        ticket = create_ticket(selected_place.row, selected_place.place_in_row)
        ticket.cinema_session = cinema_session
        tickets.append(ticket)

    db.add_multiply_objects(tickets)
    db.commit_changes()
    return Response(status_code=HTTP_200_OK)


def fill_with_default_mock(db: DataBase):
    fill_mock = FillMock(db)
    fill_mock.fill_with_default_mock()


if __name__ == "__main__":
    pass

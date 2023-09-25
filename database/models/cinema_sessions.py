from uuid import uuid4

from sqlalchemy import Column, UUID, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .shared_res import Base


class CinemaSessions(Base):
    __tablename__ = 'CinemaSessions'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    movie_id = Column('movie_id', ForeignKey('Movie.id'), nullable=False)
    cinema_hall_id = Column('cinema_hall_id', ForeignKey('CinemaHall.id'), nullable=False)

    session_start = Column('time', DateTime, nullable=False)

    # tickets = relationship('Tickets',
    #                        secondary=cinema_sessions_tickets, back_populates='cinema_sessions')
    tickets = relationship('Ticket',
                           back_populates='cinema_session')

    movie = relationship("Movie", back_populates="session_for_movie")

    hall = relationship("CinemaHall", back_populates="sessions_in_hall")

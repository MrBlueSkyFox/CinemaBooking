from uuid import uuid4

from sqlalchemy import Column, UUID, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship

from .shared_res import Base
from .cinema_sessions_tickets import cinema_sessions_tickets


class CinemaSessions(Base):
    __tablename__ = 'CinemaSessions'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    movie_id = Column('movie_id', ForeignKey('CinemaSessions.id'), nullable=False)
    cinema_hall_id = Column('cinema_hall_id', ForeignKey('CinemaSessions.id'), nullable=False)
    # tickets_id = Column('tickets_id', ForeignKey('CinemaSessions.id'), nullable=False)

    rows = Column('row', SmallInteger, nullable=False)
    place_in_row = Column('place_in_row', SmallInteger, nullable=False)

    tickets = relationship('Tickets',
                           secondary=cinema_sessions_tickets, back_populates='cinema_sessions')

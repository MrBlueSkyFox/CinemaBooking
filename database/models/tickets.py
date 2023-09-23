from uuid import uuid4

from sqlalchemy import Column, SmallInteger, UUID
from sqlalchemy.orm import relationship

from .shared_res import Base
from .cinema_sessions_tickets import cinema_sessions_tickets


class Tickets(Base):
    __tablename__ = 'Tickets'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    # session_id = Column('session_id', ForeignKey('CinemaSessions.id'), nullable=False)

    rows = Column('row', SmallInteger, nullable=False)
    place_in_row = Column('place_in_row', SmallInteger, nullable=False)

    cinema_sessions = relationship('CinemaSessions',
                                   secondary=cinema_sessions_tickets, back_populates='tickets')

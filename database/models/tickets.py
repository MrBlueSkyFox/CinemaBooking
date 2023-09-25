from uuid import uuid4

from sqlalchemy import Column, SmallInteger, UUID, ForeignKey
from sqlalchemy.orm import relationship

from .shared_res import Base


class Ticket(Base):
    __tablename__ = 'Ticket'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    session_id = Column('cinema_session_id', ForeignKey('CinemaSessions.id'), nullable=False)

    row = Column('row', SmallInteger, nullable=False)
    place_in_row = Column('place_in_row', SmallInteger, nullable=False)

    cinema_session = relationship("CinemaSessions", back_populates='tickets')
    # cinema_sessions = relationship('CinemaSessions',
    #                                secondary=cinema_sessions_tickets, back_populates='tickets')

from uuid import uuid4

from sqlalchemy import Column, UUID, SmallInteger, String

from .shared_res import Base


class CinemaHall(Base):
    __tablename__ = 'CinemaHall'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column('name', String, nullable=False)
    rows = Column('row_total', SmallInteger, nullable=False)
    places_per_row = Column('places_per_row', SmallInteger, nullable=False)

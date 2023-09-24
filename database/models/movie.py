from uuid import uuid4

from sqlalchemy import Column, UUID, LargeBinary, String
from sqlalchemy.orm import relationship

from .shared_res import Base


class Movie(Base):
    __tablename__ = 'Movie'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column('name', String, nullable=False)
    picture = Column('picture', LargeBinary, nullable=False)

    session_for_movie = relationship("CinemaSessions", back_populates="movie")

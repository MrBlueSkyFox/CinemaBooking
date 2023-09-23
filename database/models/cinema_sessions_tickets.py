from uuid import uuid4

from sqlalchemy import Column, UUID, ForeignKey, Table

from .shared_res import Base

cinema_sessions_tickets = Table(
    "CinemaSessions_Tickets",
    Base.metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid4),
    Column('cinema_session_id', UUID(as_uuid=True), ForeignKey('CinemaSessions.id'), nullable=False),
    Column('ticket_id', UUID(as_uuid=True), ForeignKey('Tickets.id'), nullable=False)
)

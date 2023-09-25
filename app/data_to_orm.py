from database.models import Ticket


def create_ticket(row, place_in_row) -> Ticket:
    return Ticket(row=row, place_in_row=place_in_row)

import datetime

today = datetime.datetime.today()
MOVIES_MOCK = [
    ("Movie_1", "data/1.jpg"),
    ("Movie_2", "data/2.jpg"),
    ("Movie_3", "data/1.jpg"),
    ("Movie_4", "data/2.jpg"),
]
CINEMA_HALL_MOCK = [
    ("RedHall", 10, 8),
    ("GreenHall", 10, 8),
    ("BlueHall", 10, 8),

]

CINEMA_SESSIONS = [
    ("Movie_1", "RedHall", today.replace(hour=12, minute=0, second=0, microsecond=0)),
    ("Movie_2", "GreenHall", today.replace(hour=14, minute=0, second=0, microsecond=0)),
    ("Movie_3", "BlueHall", today.replace(hour=16, minute=30, second=0, microsecond=0)),
    ("Movie_4", "RedHall", today.replace(hour=19, minute=0, second=0, microsecond=0)),
]

from database import DataBase


def get_db():
    db = DataBase()
    try:
        yield db
    finally:
        db.session.close()

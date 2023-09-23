from typing import Union

from sqlalchemy import create_engine, URL, MetaData
from sqlalchemy.orm import Session

from database.models import Base


class DataBase:

    def __init__(self, host: str, port: [Union[str, int]], username: str,
                 password: str, database: str, drivername: str = 'postgresql',
                 echo_debug: bool = False):
        self.engine = create_engine(URL.create(
            drivername,
            username,
            password,
            host,
            port,
            database), echo=echo_debug)
        self.session: Session = Session(self.engine, autoflush=False)
        self._dbname = database
        self._user = username
        self._password = password
        self._host = host
        self._port = port

    def create_all(self):
        Base.metadata.create_all(self.engine)
        # metadata = MetaData(self.engine)
        # metadata.create_all()

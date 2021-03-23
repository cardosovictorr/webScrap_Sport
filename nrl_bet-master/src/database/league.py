from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from src.database.base import Base


class League(Base):
    """ League ORM object that represents league of NRL.

    """
    __tablename__ = 'leagues'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    seasons = relationship('seasons')

    def __init__(self, name):
        self.name = name


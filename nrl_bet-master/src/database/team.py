from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.database.base import Base


class Team(Base):
    """ Team ORM object

    """
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    players = relationship('players')

    def __init__(self, name):
        self.year = name

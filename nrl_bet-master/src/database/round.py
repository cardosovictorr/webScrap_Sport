from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.database.base import Base


class Round(Base):
    """ Round ORM object

    """
    __tablename__ = 'rounds'

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    season_id = Column(Integer, ForeignKey('seasons.id'))
    games = relationship('games')

    def __init__(self, number):
        self.number = number


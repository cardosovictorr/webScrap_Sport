from sqlalchemy import Column, Integer, String, ForeignKey

from src.database.base import Base


class Scoring(Base):
    """ Scoring ORM object

    """
    __tablename__ = 'scoring'

    id = Column(Integer, primary_key=True)
    team = Column(String)
    tries_score = Column(Integer)
    tries_attempted = Column(Integer)




    season_id = Column(Integer, ForeignKey('games.id'))

    def __init__(self, year):
        self.year = year


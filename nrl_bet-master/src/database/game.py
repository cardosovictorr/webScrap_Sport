from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from src.database.base import Base


class Game(Base):
    """ Game ORM object

    """
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    game_date = Column(Date)
    home_score = Column(Integer)
    away_score = Column(Integer)
    round = Column(Integer, ForeignKey('rounds.id'))
    home_team = Column(Integer, ForeignKey('teams.id'))
    away_team = Column(Integer, ForeignKey('teams.id'))
    tries = relationship('tries', uselist=False, back_populates='games')
    conversions = relationship('conversions', uselist=False, back_populates='games')
    penalty_goals = relationship('penalty_goals', uselist=False, back_populates='games')

    def __init__(self, game_date, home_score, away_score):
        self.game_date = game_date
        self.home_score = home_score
        self.away_score = away_score


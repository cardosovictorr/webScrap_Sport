from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.database.base import Base


class Season(Base):
    """ Season ORM object

    """
    __tablename__ = 'seasons'

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    league = Column(Integer, ForeignKey('leagues.id'))
    rounds = relationship('rounds')

    def __init__(self, year):
        self.year = year


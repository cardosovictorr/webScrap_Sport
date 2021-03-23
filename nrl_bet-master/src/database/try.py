from sqlalchemy import Column, Integer, ForeignKey

from src.database.base import Base


class Try(Base):
    """ Try ORM object

    """
    __tablename__ = 'tries'

    id = Column(Integer, primary_key=True)
    player = Column(Integer, ForeignKey('players.id'))
    timestamp = Column(Integer)

    def __init__(self, timestamp):
        self.timestamp = timestamp

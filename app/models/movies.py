from sqlalchemy import Column
from sqlalchemy import Integer, String, Time
from sqlalchemy.orm import DeclarativeBase
from datetime import time



class Base(DeclarativeBase):
    pass


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    director = Column(String(100), nullable=False)
    length = Column(Time, nullable=False)
    rating = Column(Integer, nullable=False)


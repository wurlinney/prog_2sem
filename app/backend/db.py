from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine


engine = create_engine('sqlite:///project.db', echo=True)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass

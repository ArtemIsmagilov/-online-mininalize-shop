import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from ..settings import Conf

engine = sa.create_engine(Conf.DATABASE_URI, echo=True)

LocalSession = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


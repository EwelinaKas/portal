from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    fullname = Column(String(50))
    lastname = Column(String(50))
    nickname = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    registration_date = Column(DateTime, default=datetime.now)

    class Hashtag(Base):
        __tablename__ = "hashtags"

        id = Column(Integer, primary_key=True)
        name = Column(String(50), unique=True, nullable=False)
        creation_date = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"User({self.nickname})"

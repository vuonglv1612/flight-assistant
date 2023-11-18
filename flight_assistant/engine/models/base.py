import uuid

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base


class Base:
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))


Base = declarative_base(cls=Base)

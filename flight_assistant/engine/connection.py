from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_session_factory(uri):
    engine = create_engine(uri)
    session_factory = sessionmaker(bind=engine)
    return session_factory

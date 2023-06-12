from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///instagram.db',connect_args={'check_same_thread':False})
base = declarative_base()
session_maker = sessionmaker(bind=engine , autoflush=False , autocommit=False)

def get_db():
    session = session_maker()
    try:
        yield session
    finally:
        session.close()

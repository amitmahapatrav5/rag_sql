# src/db/session.py
from sqlalchemy.orm import Session
from db.conn import engine

def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
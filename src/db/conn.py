from sqlalchemy import create_engine


# you can hit sqlite3.ProgrammingError: 
# SQLite objects created in a thread can only be used in that same thread.
engine = create_engine("sqlite:///./test.db", echo=True)
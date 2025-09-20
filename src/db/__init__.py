from db.models import Base
from db.conn import engine


Base.metadata.create_all(engine)
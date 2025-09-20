from typing import List, Dict

from sqlalchemy import select
from sqlalchemy.orm import Session

from db.conn import engine
from db.models import File


def add_owner_specific_file(owner: str, name: str):
    with Session(engine) as session:
        file = File(owner=owner, name=name)
        # It only inserts; duplicates are allowed. 
        # If you intend upsert behavior, you’ll need a unique constraint on (owner, name) 
        # and conflict handling.
        session.add(file)
        session.commit()

def get_owner_specific_files(owner: str):
    with Session(engine) as session:
        stmt = select(File).where(File.owner==owner)
    return { 'files': [{'name' : file.name} for file in session.scalars(stmt)] }

def remove_owner_specific_file(owner: str, name: str):
    with Session(engine) as session:
        file = session.query(File).filter_by(owner=owner, name=name).first()
        if file is not None:
            session.delete(file) # file could be None -> crashes
            session.commit()
        return
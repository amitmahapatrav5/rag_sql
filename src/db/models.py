from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

# Table is 'File' (capital F). Not wrong, but sometimes better to use lowercase files. 
# Also consider indexes/constraints.
# Add a unique constraint to prevent duplicates

class File(Base):
    __tablename__ = 'File'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    owner: Mapped[str]
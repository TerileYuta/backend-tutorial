from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy import Index
from sqlalchemy.types import INTEGER, String
from sqlalchemy import create_engine
from config import settings

Base = declarative_base()

class StudentsTable(Base):
    __tablename__ = "students"

    id = Column(
        INTEGER,
        primary_key=True,
    )
    name = Column(  
        String,
        nullable=False
    )
    grade = Column(  
        INTEGER,
        nullable=False
    )

    __table_args__ = (
        Index("id", id),
    )

engine = create_engine(settings.db_url)
Base.metadata.create_all(engine)
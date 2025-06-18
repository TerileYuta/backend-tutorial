from sqlalchemy.orm import sessionmaker
from model import engine

SessionClass = sessionmaker(engine)
session = SessionClass()
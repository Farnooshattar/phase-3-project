from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///events_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

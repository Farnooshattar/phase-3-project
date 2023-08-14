from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

from prettycli import green, color

Base = declarative_base()
engine = create_engine("sqlite:///events_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String(25), unique=True)
    email = Column(String(55))
    birthday = Column(DateTime)

    # One-to-many relationship with Event
    events = relationship("Event", backref="user")

    def __repr__(self):
        id = str(self.id)
        birthday = str(self.birthday)

        return \
            green(f"\n<User ") + \
            color(f"id={color(id).rgb_fg(132, 209, 50)}, ").rgb_fg(83, 36, 224) + \
            color(f"first_name={color(self.first_name).rgb_fg(132, 209, 50)}, ").rgb_fg(83, 36, 224) + \
            color(f"last_name={color(self.last_name).rgb_fg(132, 209, 50)}, ").rgb_fg(83, 36, 224) + \
            color(f"username={color(self.username).rgb_fg(132, 209, 50)}, ").rgb_fg(83, 36, 224) + \
            color(f"email={color(self.email).rgb_fg(132, 209, 50)}, ").rgb_fg(83, 36, 224) + \
            color(f"birthday={color(birthday).rgb_fg(132, 209, 50)}").rgb_fg(83, 36, 224) + \
            green(">")


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    date_time = Column(DateTime)
    # Many-to-one relationship with User
    user_id = Column(Integer, ForeignKey('users.id'))
    # user = relationship("User", back_populates="events")

    def __repr__(self):
        id_str = str(self.id)
        # Format the datetime object as a string
        date_time_str = self.date_time.strftime('%Y-%m-%d %H:%M:%S')

        return \
            green(f"\n<Event ") + \
            color(f"id={color(id_str).rgb_fg(132, 209, 50)}, ").rgb_fg(83, 36, 224) + \
            color(f"title={color(self.title).rgb_fg(132, 209, 50)}, ").rgb_fg(83, 36, 224) + \
            color(f"description={color(self.description).rgb_fg(132, 209, 50)}, ").rgb_fg(83, 36, 224) + \
            color(f"date_time={color(date_time_str).rgb_fg(132, 209, 50)}").rgb_fg(83, 36, 224) + \
            green(">")

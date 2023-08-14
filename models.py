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

    events = relationship('Event', back_populates='users')

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
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='events')

    def __repr__(self):
        id = str(self.id)

        return \
            green(f"\n<Event ") + \
            color(f"id={color(id).rgb_fg(132, 209, 50)}, ").rgb_fg(83, 36, 224) + \
            color(f"title={color(self.title).rgb_fg(132, 209, 50)}, ").rgb_fg(83, 36, 224) + \
            color(f"description={color(self.description).rgb_fg(132, 209, 50)}, ").rgb_fg(83, 36, 224) + \
            color(f"date_time={color(self.date_time).rgb_fg(132, 209, 50)}").rgb_fg(83, 36, 224) + \
            green(">")
#     @classmethod
#     def add_user(cls, first_name):

#         user = User(first_name=first_name)
#         session.add(user)
#         session.commit()
#         return user


# user = User.add_user("Bob")
# user = User.add_user("Sue")

# session.commit()


# last_name = Column(String)
# email = Column(String, unique=True)
# phone_number = Column(String)
# address = Column(String)
# city = Column(String)
# state = Column(String)
# zip_code = Column(String)

# events = relationship("event", backref="user")
# user = session.query(cls).filter(
#     cls.first_name.like(first_name)).first()
# if user:
#     return user
# else:

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import ipdb
from prettycli import green, color
import datetime
from session import session


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
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

    @classmethod
    def find_by(cls, email):
        user = session.query(cls).filter(cls.email.like(email)).first()
        if user:
            return user
        else:
            # user = User(email=email)
            # session.add(user)
            # session.commit()
            return False

    @classmethod
    def Add_user_by(cls, email):
        user = User(email=email)
        session.add(user)
        session.commit()
        # print(user)
        return user


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

    @classmethod
    def find_events_by(cls, user_id):
        # print(session.query(cls).filter(cls.user_id == user_id).all())
        return session.query(cls).filter(cls.user_id == user_id).all()

    @classmethod
    def add_new_event(cls, user_id, title, description, date_time):
        # ipdb.set_trace()
        event = Event(title=title, description=description,
                      date_time=date_time, user_id=user_id)
        session.add(event)
        session.commit()
        return event

    @classmethod
    def show_first_event(cls, user_id):
        return (session.query(cls).filter(cls.user_id ==
                                          user_id).order_by(cls.date_time.asc()).first())

    @classmethod
    def edit_event(cls, event_id, title, description, date_time):
        event = session.query(cls).filter_by(id=event_id).first()
        if event:
            event.title = title
            event.description = description
            event.date_time = date_time
            session.commit()
            return event
        else:
            return None

    @classmethod
    def find_missed_events(cls, user_id):
        current_datetime = datetime.datetime.now()

        return session.query(cls).filter(cls.user_id == user_id, cls.date_time < current_datetime).all()

    @classmethod
    def show_upcoming_events(cls, user_id):
        upcoming_events = {}
        current_datetime = datetime.datetime.now()
        for event in Event.find_events_by(user_id):
            if event.date_time > current_datetime:
                days_until_event = (event.date_time - current_datetime).days
                if days_until_event not in upcoming_events:
                    # populates the dictionary
                    upcoming_events[days_until_event] = []
                upcoming_events[days_until_event].append(event)

        if upcoming_events:
            print("Upcoming Events:")
            for days_until_event, events in sorted(upcoming_events.items()):
                print(f"\n{days_until_event} days from now:")
                for event in events:
                    print(f"- {event.title} on {event.date_time}")
        else:
            print("No upcoming events found.")

    @classmethod
    def delete_event(cls, event_id):
        event = session.query(cls).filter_by(id=event_id).first()
        if event:
            session.delete(event)
            session.commit()
            return True
        else:
            return False

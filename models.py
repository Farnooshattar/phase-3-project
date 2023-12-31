from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from prettycli import green, color
import datetime

Base = declarative_base()
engine = create_engine("sqlite:///events_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)


class User(Base):  # users table
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String(25), unique=True)
    email = Column(String(55))
    birthday = Column(DateTime)

    # Class has a One-to-many relationship with Event
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
            return user  # returns a row of the user info
        else:
            return False

    @classmethod
    def Add_user_by(cls, email):
        user = User(email=email)
        session.add(user)
        session.commit()
        return user


class Event(Base):  # events table
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    date_time = Column(DateTime)
    # Many-to-one relationship with User
    user_id = Column(Integer, ForeignKey('users.id'))

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
    # ids are indexed, so this is a fast retreival of the events!
    def find_events_by(cls, user_id):
        return session.query(cls).filter(cls.user_id == user_id).all()

    @classmethod
    def add_new_event(cls, user_id, title, description, date_time):
        event = Event(title=title, description=description,
                      date_time=date_time, user_id=user_id)
        session.add(event)
        session.commit()
        return event

    @classmethod
    def show_upcoming_events(cls, user_id):
        # creates an empty dictionary to store the upcoming events
        # grouped by the number of days until they occur
        upcoming_events = {}
        current_datetime = datetime.datetime.now()
        for event in Event.find_events_by(user_id):
            if event.date_time > current_datetime:
                days_until_event = (event.date_time - current_datetime).days
                # checks if the calculated days_until_event is already a key
                if days_until_event not in upcoming_events:
                    # If not, a new empty list is added as the value for that key
                    upcoming_events[days_until_event] = []
                upcoming_events[days_until_event].append(event)
        # Check if there are any upcoming events in the upcoming_events dictionary
        if upcoming_events:
            print("Upcoming Events:")
            # Loop through the upcoming_events dictionary sorted by the number of days until each event
            for days_until_event, events in sorted(upcoming_events.items()):
                # Print the header indicating the number of days until the event
                print(f"\n{days_until_event} days from now:")
                # Loop through the events occurring on the same number of days until the event
                for event in events:
                    # Display event details with its title and date
                    print(f"- {event.title} on {event.date_time}")
        else:
            # If there are no upcoming events, print a message indicating so
            print("No upcoming events found.")

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
        # filters out the events that are passed according to current dateand time
        return session.query(cls).filter(cls.user_id == user_id, cls.date_time < current_datetime).all()

    @classmethod
    def delete_event(cls, event_id):
        event = session.query(cls).filter_by(id=event_id).first()
        if event:
            session.delete(event)
            session.commit()
            return True
        else:
            return False

from models import User, Event
import ipdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from faker import Faker
from datetime import datetime

engine = create_engine("sqlite:///events_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

users = []
events = []

# Delete existing data
session.query(Event).delete()
session.query(User).delete()
session.commit()

# Create users
for i in range(10):
    fake_first = fake.first_name()
    fake_last = fake.last_name()
    fake_email = fake.email()
    user = User(
        first_name=fake_first,
        last_name=fake_last,
        username=f"{fake_first}_{fake_last}",
        email=fake_email,
        birthday=datetime.strptime(fake.date(), '%Y-%m-%d').date()
    )
    users.append(user)
    session.add(user)
    session.commit()

# Create events for each user
for user in users:
    for j in range(5):
        event = Event(
            title=fake.sentence(),
            description=fake.paragraph(),
            date_time=fake.date_time_between(start_date='-1y', end_date='now'),
            user_id=user.id  # Associate the event with the current user
        )
        events.append(event)


# Bulk save users and events
# session.bulk_save_objects(users)
session.bulk_save_objects(events)
session.commit()

# for user in users:
#     print(f"User: {user}")
#     for event in user.events:
#         print(f"    Event: {event}")
ipdb.set_trace()
print(session.query(Event).first().user_id)
print(session.query(User).first().events)

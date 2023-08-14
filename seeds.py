from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from faker import Faker
from datetime import datetime


engine = create_engine("sqlite:///events_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

users = []

for i in range(100):

    fake_first = fake.first_name()
    fake_last = fake.last_name()
    fake_email = fake.email()
    users.append(
        User(
            first_name=fake_first,
            last_name=fake_last,
            username=f"{fake_first}_{fake_last}",
            email=fake_email,
            birthday=datetime.strptime(fake.date(), '%Y-%m-%d').date()
        )
    )
print(users)
session.query(User).delete()
session.commit()


session.bulk_save_objects(users)
session.commit()

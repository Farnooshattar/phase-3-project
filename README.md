# phase-3-project

Event Calendar CLI and Database Seeding

This repository includes a Command Line Interface (CLI) application for managing events within a calendar. Additionally, the repository features a script for seeding the database with sample data. Migrations are performed using alembic.

Event Calendar CLI
The cli.py file contains a CLI application that lets users manage their calendar events. Users can log in, sign up, view their events, create new events, edit existing events, and perform various other actions using lists and dictionaries. The CLI interacts seamlessly with an SQLite database to store and organize user and event data.

To run the CLI, execute the following command: python cli.py
The CLI is designed with a menu navigation system that enables users to navigate options using arrow keys and the Enter key.
Database Seeding Script
In the repository, the seeds.py script serves the purpose of populating the SQLite database with simulated data. Utilizing the Faker library, the script generates fictional user and event details. This script demonstrates the implementation of data seeding using SQLAlchemy.

To seed the database with sample data, execute the following command: python seeds.py
Upon execution, the script will automatically create and insert fabricated user and event data into the database. The schema of the database is constructed using SQLAlchemy, and this seeding script illustrates how to initialize a database with initial data.

Usage Guidelines
Run the cli.py script to launch the Event Calendar CLI.
Utilize the CLI to log in, sign up, manage events, and perform various tasks.
Optionally, execute the seeds.py script to populate the database with mock data for testing and exploration.
It's important to note that this implementation is simplified. For production usage, consider incorporating additional features, robust error handling, and enhanced security measures.

For inquiries or assistance, please feel free to contact the developer at attarfarnoosh@gmail.com.

#developer notes to self

1. create virtual environment, first created the project in github (then in terminal:pipenv --python 3.9.2, because my python version is 3.9.2 retrieved from python --version)
2. install dependencies (run: pipenv install sqlalchemy==1.4.41 alembic ipdb faker)
   a. SQLAlchemy 1.4.41
   b. Alembic (migration manager)
   c. ipdb
   d. faker (to generate fake data)
3. create the migration environmet (after pipenv shell, alembic init migrations)
4. to configure the migration environmet (alembic.ini and env.py) (sqlalchemy.url = sqlite:///events_tracker.db) (made some updates to env.py)
5. make a new file called models.py in the main root and create the declarative_base
6. create schema (python classes or models)
7. populate the database with seeds
8. test the relationships (one to many in this project)

# alembic commnads

# alembic revision --autogenerate -m "update users to user"

# alembic upgrade head

# alembic downgrade -1

# alembic downgrade Base

# session.query(User).first().events, session.query(User).first().email, session.query(Event).first().user, session.query(User).get(1)

# session.query(User).filter(User.email.like("vwallace@example.org")).first()

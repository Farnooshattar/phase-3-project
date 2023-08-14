# phase-3-project

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

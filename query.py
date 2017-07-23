from sqlalchemy_declarative import Student, Base
from sqlalchemy import create_engine
engine = create_engine('sqlite:///students.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
# Make a query to find all Persons in the database
print(session.query(Student).filter(Student.firstName == 'Jane').first().email)
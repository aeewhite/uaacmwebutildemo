from sqlalchemy_declarative import Student, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from person import Person
import csv

def populateStudentList(responses, studentRegistrations):
    for response in responses:
        firstName = ''
        lastName = ''
        email = ''
        slack = ''
        size = ''
        for answer in response.answers:
            if (answer.question_id == 'textfield_9999'):
                firstName = answer.answer
            elif (answer.question_id == 'textfield_9999'):
                lastName = answer.answer
            elif (answer.question_id == 'email_9999'):
                email = answer.answer
            elif (answer.question_id == 'yesno_9999'):
                slack = answer.answer
            elif (answer.question_id == 'dropdown_9999'):
                size = answer.answer
        studentRegistrations.append(Person(firstName, lastName, email, slack, size))
    return studentRegistrations

def startDBSession(engine):
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()
    return session

def createEngine():
    return create_engine('sqlite:///students.db')

def addStudentToDb(engine, session, student):
    Base.metadata.bind = engine
    new_student = Student(firstName=student.firstName, lastName=student.lastName, email=student.email, slack=student.slack, size=student.size)
    session.add(new_student)
    return session

def exportDbToCsv(session):
    outfile = open('memberList.csv', 'w')
    outcsv = csv.writer(outfile)
    records = session.query(Student).all()
    [outcsv.writerow([getattr(curr, column.name) for column in Student.__mapper__.columns]) for curr in records]
    outfile.close()
from person import Person
from emailmanager import *
from studentdbutil import *
from sqlalchemy_declarative import Base
import typeform
import datetime
import time

form = typeform.Form(api_key='bamboozled', form_id='99999')

engine = createEngine()

f=open('log.html', 'w')
f.write('<html>Awoke at ' + str(datetime.datetime.now()) + '</html>\n')

while 1:
    server = establishConnection()
    if datetime.datetime.now().hour == 20 and datetime.datetime.now().minute == 0:
        sendMemberList(server)

    studentRegistrations = []

    responses = form.get_responses(limit=100, since=1487863154)

    studentRegistrations = populateStudentList(responses, studentRegistrations)

    session = startDBSession(engine)

    for student in studentRegistrations:
        Base.metadata.bind = engine
        exists = session.query(Student).filter(Student.email == student.email).count()
        if exists == 0:
            sendAcknowledgement(server, student.firstName, student.lastName, student.email, student.slack)
            session = addStudentToDb(engine, session, student)
    
    session.commit()

    exportDbToCsv(session)

    f.write('<html>Still alive at ' + str(datetime.datetime.now()) + '</html>')
    f.close()
    time.sleep(10)
    f = open('log.html', 'w')
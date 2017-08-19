import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime
from static import *

def establishConnection():
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(FROM_EMAIL(), PASSWORD())
    return server

def sendMemberList(server):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'updated member list ' + str(datetime.datetime.now())
    msg['From'] = FROM_EMAIL()
    msg['To'] = FROM_EMAIL()
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("memberList.csv", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="memberList.csv"')
    msg.attach(part)
    server.sendmail(FROM_EMAIL(), FROM_EMAIL(), msg.as_string())

def sendAcknowledgement(server, firstName, lastName, email, slack):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Demo Email'
    msg['From'] = FROM_EMAIL()
    msg['To'] = email
    body = '<h2>Hello world!</h2><br>'
    body_container = MIMEMultipart('alternative')
    body_container.attach(MIMEText(body.encode('utf-8'), 'html', 'UTF-8'))
    msg.attach(body_container)
    server.sendmail(FROM_EMAIL(), email, msg.as_string())
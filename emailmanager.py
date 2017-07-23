import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime

def establishConnection():
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login('example@gmail.com', 'password')
    return server

def sendMemberList(server):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'updated member list ' + str(datetime.datetime.now())
    msg['From'] = 'example@gmail.com'
    msg['To'] = 'example@gmail.com'
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("memberList.csv", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="memberList.csv"')
    msg.attach(part)
    server.sendmail('example@gmail.com', 'example@gmail.com', msg.as_string())

def sendAcknowledgement(server, firstName, lastName, email, slack):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Welcome to UA ACM'
    msg['From'] = 'example@gmail.com'
    msg['To'] = email
    body = '<h2>We\'re glad to have you on board!</h2><br>'
    if slack == '1':
        body += '<a href=\"https://unofficialuacs.slack.com/signup?email=' + email.split('@')[0] + '\">Complete Slack registration</a><br><br>'
    body += '<a href=\"mailto:listserv@bama.ua.edu?body=subscribe%20ua-acm%20' + firstName + '%20' + lastName + '\">Send message to listserv to get our emails</a><br>(if email links aren\'t you\'re thing, manually email listserv@bama.ua.edu with the message \'subscribe ua-acm\')'
    body_container = MIMEMultipart('alternative')
    body_container.attach(MIMEText(body.encode('utf-8'), 'html', 'UTF-8'))
    msg.attach(body_container)
    server.sendmail('example@gmail.com', email, msg.as_string())
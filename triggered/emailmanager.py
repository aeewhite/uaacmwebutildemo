import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from static import *

def establishConnection():
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(FROM_EMAIL(), PASSWORD())
    return server

def sendAcknowledgement(firstName, lastName, email, slack):
    server = establishConnection()
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Welcome to UA ACM'
    msg['From'] = FROM_EMAIL()
    msg['To'] = email
    body = '<h2>We\'re glad to have you on board!</h2><br>'
    if slack == '1' or slack == 'Yes':
        body += '<a href=\"https://unofficialuacs.slack.com/signup?email=' + email.split('@')[0] + '\">Complete Slack registration</a><br><br>'
    body += '<a href=\"mailto:listserv@bama.ua.edu?body=subscribe%20ua-acm%20' + firstName + '%20' + lastName + '\">Send message to listserv to get our emails</a><br><small>(if email links aren\'t you\'re thing, manually email listserv@bama.ua.edu with the message \'subscribe ua-acm ' + firstName + ' ' + lastName +'\')</small>'
    body_container = MIMEMultipart('alternative')
    body_container.attach(MIMEText(body.encode('utf-8'), 'html', 'UTF-8'))
    msg.attach(body_container)
    server.sendmail(FROM_EMAIL(), email, msg.as_string())
    server.quit()

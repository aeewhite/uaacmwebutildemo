from flask import Flask, request, render_template
from emailmanager import *

app = Flask(__name__)

@app.route('/formsubmit', methods=['POST'])
def result():
    items = request.get_json()
    sendAcknowledgement(items['firstName'], items['lastName'], items['email'], items['slack'])
    return "Thanks!"
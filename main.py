import os
import json
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def landingpage():
    with open('agencies.json') as fp:    
        agencies = json.load(fp)
    context = {'agencies': agencies}
    return render_template('landing.html', **context)

from flask import Flask
from flask_ask import Ask, statement, question, session

import random
import string
import json
import requests
import time


app = Flask(__name__)
ask = Ask(app, "/reddit_reader")

def get_headlines():
    pass

@app.route('/')
def homepage():
    return "hi there, how ya doin?"

@ask.launch
def start_skill():
    welcome_message = 'Hello there, would you like the news?'
    return question(welcome_message)

@ask.intent("YesIntent")
def share_headlines():
    headlines = get_headlines()
    headline_msg = 'The current world news headlines are {}'.format(headlines)
    return statement(headline_msg)

@ask.intent("NoIntent")
def no_intent():
    bye_msg = 'You make me sad. Bye'
    return statement(bye_msg)




if __name__ == '__main__':
    app.run(debug = True)


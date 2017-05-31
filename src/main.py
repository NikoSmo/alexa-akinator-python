from src import akinatorAPI
from flask import Flask
from flask_ask import Ask, statement, question, session

import random
import string
import json
import requests
import time

app = Flask(__name__)
ask = Ask(app, "/")

SKILL_NAME="Akina"

answers = { 'yes': '0', 'no' : '1', 'dontKnow' : '2', 'probably' : '3', 'probablyNot' : '4'}

aki = akinatorAPI.Apinator()

@ask.launch
def start_skill():
    aki.new_session('dawn')
    welcome_message = 'Willkommen bei Akina. Lass uns beginnen.'
    return question(welcome_message + aki.getQuestion())

@ask.intent("AMAZON.YesIntent")
def next_question():
    if not aki.isCharacterFound():
        aki.sendAnswer(answers['yes'])
        return question(aki.getQuestion())
    else:
        return question(aki.getCharacterGuess())

@ask.intent("AMAZON.NoIntent")
def next_question():
    if not aki.isCharacterFound():
        aki.sendAnswer(answers['no'])
        return question(aki.getQuestion())
    else:
        return question(aki.getCharacterGuess())

@ask.intent("ProbablyIntent")
def next_question():
    if not aki.isCharacterFound():
        aki.sendAnswer(answers['probably'])
        return question(aki.getQuestion())
    else:
        return question(aki.getCharacterGuess())

@ask.intent("ProbablyNotIntent")
def next_question():
    if not aki.isCharacterFound():
        aki.sendAnswer(answers['probablyNot'])
        return question(aki.getQuestion())
    else:
        return question(aki.getCharacterGuess())

@ask.intent("DontKnowIntent")
def next_question():
    if not aki.isCharacterFound():
        aki.sendAnswer(answers['dontKnow'])
        return question(aki.getQuestion())
    else:
        return question(aki.getCharacterGuess())

@ask.intent("StopIntent")
def stop_intent():
    bye_msg = "Bis zum nächsten mal."
    return statement(bye_msg);

@ask.intent("AMAZON.CancelIntent")
def stop_intent():
    bye_msg = "Bis zum nächsten mal."
    return statement(bye_msg);

if __name__ == '__main__':
    app.run(debug = True)
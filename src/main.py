import akinatorAPI
from flask import Flask
from flask_ask import Ask, statement, question, session

import logging
from random import *
import string
min_char = 8
max_char = 12
allchar = string.ascii_letters + string.digits

app = Flask(__name__)
ask = Ask(app, "/akina")

# log = logging.getLogger()
# log.addHandler(logging.StreamHandler())
# log.setLevel(logging.DEBUG)
# logging.getLogger("flask_ask").setLevel(logging.DEBUG)

SKILL_NAME = "Akina"
reprompt_msg = "Entschuldigung, ich habe dich nicht verstanden. "
character_found_msg = "Ich denke deine Figur ist : "


answers = {'yes': '0', 'no': '1', 'dontKnow': '2', 'probably': '3', 'probablyNot': '4'}

aki = akinatorAPI.Apinator()


@app.route("/")
def homepage():
    return "Akina is running. . ."


@ask.launch
def start_skill():
    session_name = "".join(choice(allchar) for _ in range(randint(min_char, max_char)))
    aki.new_session(session_name)
    welcome_message = 'Willkommen bei Akina. Möchtest du ein Spiel starten?'
    return question(aki.getQuestion()).reprompt(aki.getQuestion())


@ask.intent("AMAZON.YesIntent")
def next_question():
    print("ja")
    if not aki.isCharacterFound():
        aki.sendAnswer(answers['yes'])
        return question(aki.getQuestion()).reprompt(aki.getQuestion())
    else:
        print("I'm guessing now")
        return question(character_found_msg + aki.getCharacterGuess())


@ask.intent("AMAZON.NoIntent")
def next_question():
    print("nein")
    if not aki.isCharacterFound():
        aki.sendAnswer(answers['no'])
        return question(aki.getQuestion()).reprompt(aki.getQuestion())
    else:
        return question(character_found_msg + aki.getCharacterGuess())


@ask.intent("ProbablyIntent")
def next_question():
    print("vielleicht")
    if not aki.isCharacterFound():
        aki.sendAnswer(answers['probably'])
        return question(aki.getQuestion()).reprompt(aki.getQuestion())
    else:
        return question(character_found_msg + aki.getCharacterGuess())


@ask.intent("ProbablyNotIntent")
def next_question():
    print("wahrscheinlich nicht")
    if not aki.isCharacterFound():
        aki.sendAnswer(answers['probablyNot'])
        return question(aki.getQuestion()).reprompt(aki.getQuestion())
    else:
        return question(character_found_msg + aki.getCharacterGuess())


@ask.intent("DontKnowIntent")
def next_question():
    print("weiß ich nicht")
    if not aki.isCharacterFound():
        aki.sendAnswer(answers['dontKnow'])
        return question(aki.getQuestion()).reprompt(aki.getQuestion())
    else:
        return question(character_found_msg + aki.getCharacterGuess())


@ask.intent("StopIntent")
def stop_intent():
    bye_msg = "Bis zum nächsten mal."
    return statement(bye_msg)


@ask.intent("AMAZON.CancelIntent")
def stop_intent():
    bye_msg = "Bis zum nächsten mal."
    return statement(bye_msg)


if __name__ == '__main__':
    app.run(debug=True)

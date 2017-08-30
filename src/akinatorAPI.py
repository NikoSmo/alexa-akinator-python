import urllib.parse
import requests
import json
import time
import random


class Apinator:
    def __init__(self):
        self.base_url = 'http://api-de1.akinator.com/ws/'
        self.url = ''
        self.session = ''
        self.json_data = ''
        self.signature = ''
        self.step = 0
        self.answerId = ''
        self.question = ''
        self.characterFound = False
        self.progression_threshold = 93

    def new_session(self, name):
        self.url = self.base_url + 'new_session?partner=1&' + \
            urllib.parse.urlencode({'player': name})
        self.json_data = requests.get(self.url).json()
        self.session = self.json_data['parameters']['identification']['session']
        self.signature = self.json_data['parameters']['identification']['signature']
        self.question = self.json_data['parameters']['step_information']['question']
        print(self.url)

    def sendAnswer(self, answerId):
        self.answerId = answerId
        self.url = self.base_url + 'answer?session=' + self.session + '&signature=' + \
            self.signature + '&step=' + str(self.step) + '&answer=' + self.answerId
        self.json_data = requests.get(self.url).json()
        if (self.json_data['completion'] == 'OK'):
            self.progression = float(self.json_data['parameters']['progression'])
            if self.progression > self.progression_threshold:
                self.characterFound = True
            self.question = self.json_data['parameters']['question']
            self.step += 1

    def getCharacterGuess(self) -> object:
        self.url = self.base_url + 'list?session=' + self.session + '&signature=' + self.signature \
            + '&step=' + \
            str(self.step) + '&size=2&max_pic_width=246&max_pic_height=294&pref_photos=OK-FR&mode_question=0'
        self.json_data = requests.get(self.url).json()
        self.character = self.json_data['parameters']['elements'][0]['element']['name']
        return self.character

    def getQuestion(self):
        return self.question

    def isCharacterFound(self):
        return self.characterFound

    def characterGuessWrong(self):
        self.characterFound = False
        if self.progression_threshold < 100:
            self.progression_threshold += 1

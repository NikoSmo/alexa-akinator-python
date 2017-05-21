import random
import time

from src import akinatorAPI

api = akinatorAPI.Apinator()
api.new_session('dawn')
api.getQuestion()

while not api.isCharacterFound():
    number = random.randint(0,4)
    api.sendAnswer(str(number))
    api.getQuestion()

api.getCharacterGuess()
time.sleep(2)
api.characterGuessWrong()
while not api.isCharacterFound():
    api.sendAnswer('0')
    api.getQuestion()

api.getCharacterGuess()
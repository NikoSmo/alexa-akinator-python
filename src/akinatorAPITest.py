import random
import time

from src import akinatorAPI

api = akinatorAPI.Apinator()
api.new_session('dawn')
api.getQuestion()

while not api.isCharacterFound():
    number = random.randint(0,0)
    api.sendAnswer(str(number))
    api.getQuestion()
print("Your Character is : ")
api.getCharacterGuess()

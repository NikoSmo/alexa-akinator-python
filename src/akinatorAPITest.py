import random
import time
import os
from src import akinatorAPI

api = akinatorAPI.Apinator()
api.new_session('dawn')
api.getQuestion()

while not api.isCharacterFound():
    number = random.randint(0,0)
    api.sendAnswer(str(number))
    api.printQuestion()
print("Your Character is : ")
api.getCharacterGuess()

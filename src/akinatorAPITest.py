import random
import time
import os
import akinatorAPI

api = akinatorAPI.Apinator()
api.new_session('dawn')
print(api.getQuestion())

while not api.isCharacterFound():
    number = random.randint(0, 0)
    api.sendAnswer(str(number))
    print(api.getQuestion())
print("Your Character is : {}".format(api.getCharacterGuess()))

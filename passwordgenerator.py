import random
import string
import win32api

LETTERS = string.ascii_letters
NUMS = '0123456789'
SPE = '-_.:,;+*@£$%?!€'
SYMBOLS = LETTERS + NUMS + SPE
palavrapasse = '12'
len = 2

def code():
    attempt = ''.join(random.sample(SYMBOLS, len))
    count = 0
    while (attempt != palavrapasse):
        attempt = ''.join(random.sample(SYMBOLS, len))
        print(attempt)
        count = count + 1
        if (attempt == palavrapasse):
            print("Password was: " + palavrapasse)
            print("Number of attempts: " + str(count))
            win32api.MessageBox(0, 'Password found', 'Message', 0x00001000)

code()

def generatorpass():
    for i in range(1, 5):
        password = ''.join(random.sample(SYMBOLS, len))
        print("Password option " + str(i) + " : " + password)
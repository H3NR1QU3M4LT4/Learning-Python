import random
import string

LETTERS = string.ascii_letters
NUMS = '0123456789'
SPE = '-_.:,;+*@£$%?!€'
SYMBOLS = LETTERS + NUMS + SPE
len = 25
for i in range(1,5):
    password = ''.join(random.sample(SYMBOLS , len))
    print ("Password option " + str(i) + " : " + password) 
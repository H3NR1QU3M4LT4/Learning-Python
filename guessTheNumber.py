#é gerado um numero e o objetivo é adivinha-lo
import random

number = random.randint(1,20) #gerar um numero aleatorio entre 1 e 20
print('I am thinking of a number between 1 and 20.')

for guesses in range (0,6):
    print('Take a guess')
    guess = int(input()) #variavél que guarda o valor inserido força a ser inteiro
    
    if guess < 1 :
        print('Number not acceptable! The number is between 1 and 20.')
    elif guess > 20 :
        print('Number not acceptable! The number is between 1 and 20.')
    elif guess > number :
        print('Your number is high')
    elif guess < number :
        print('Your number is low')
    
    else :
        break #condição verdadeira, significa que o numero do input é igual ao numero gerado random

if guess == number :
    print('Good job! You guessed my number in ' + str(guesses) + ' guesses! And the number was: ' + str(number))
else:
    print('Nope. The number I was thinking of was ' + str(number))


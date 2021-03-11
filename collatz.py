def collatz (number):
    while number != 1:
        if number % 2 == 0 :
            number = number // 2
            print (number)
        elif number % 2 == 1 :
            number = (number * 3) + 1 
            print (number)

numberInput = 0
while numberInput != isinstance and numberInput == 0 :
    print ('Insert a random number!')
    try:
        numberInput = int(input())
    except ValueError:
        print('Error: Invalid argument. We need a number not a declaration of love!!')

collatz(numberInput)
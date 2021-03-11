#chapter 4

def cats():
    catNames = [] #cria uma lista
    while True:
        print('Enter the name of cat ' + str(len(catNames) + 1) + '(Or enter nothing to stop.):')
        name = input()
        if name == '':
            break
        catNames = catNames + [name] # concatenação de lista
    print('The cat names are:')
    for name in catNames:
        print(' ' + name)
cats()

def example():
    supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
    for i in range(len(supplies)):
        print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
#example()

def myPets():
    myPets = ['Zophie', 'Pooka', 'Fat-tail']
    print(myPets)
    print('Enter a pet name:')
    name = input()
    if name not in myPets:
        print('I do not have a pet named ' + name)
    else:
        print(name + ' is my pet.')
#myPets()

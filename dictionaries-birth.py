def birthday():
    birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
    print("Actual:" + str(birthdays))
    print()
    while True:
        print('Enter a name: (blank to quit)')
        name = input()
        if name == '':
            break
        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
        else:
            print('I do not have birthday information for ' + name)
            print('What is their birthday?')
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated.')
            print("Update:" + str(birthdays))
#birthday()

def dict():
    spam = {'color': 'red', 'age': 42}
    print(spam.keys())
    print(list(spam.keys()))

    print()
    for v in spam.values():
        print(v)

    print()

    for k in spam.keys():
        print(k)

    print()

    for i in spam.items():
        print(i)

#dict()

def dicts():
    spam = {'color': 'red', 'age': 42}
    for k, v in spam.items():
        print('Key: ' + k + ' Value: ' + str(v))
    
    print('color' in spam.keys())
    print('fds' in spam.keys())
    print('fds' not in spam) #spam.keys() or spam.values()
    print('color' in spam.values())
    print('red' in spam.values())
dicts()
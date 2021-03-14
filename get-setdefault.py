import pprint

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
print (spam)

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
contador = 0
for character in message:
    contador = contador + 1
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)
pprint.pprint(count)
print('NUMBER OF CHARACTER: ' + str(contador))

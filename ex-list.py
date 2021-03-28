oldList = []
# damn
def listNew():
    global oldList
    while True:
        print('Enter or list of things:')
        thing = input()
        if thing == '':
            break
        oldList = oldList + [thing] # concatenação de lista

def changeList(list):
    print(list)
    blanc = ''
    for i in range(int(len(list) -2)):
        blanc = blanc + list[i]
        blanc = blanc + ', '
        print(blanc + list[-2] + ' and ' + list[-1])

listNew()
changeList(oldList)

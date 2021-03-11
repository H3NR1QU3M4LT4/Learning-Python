def some():
    print(chiken)
chiken = 10
some()
print(chiken)

def sameName1():
    carrots = 'carrots local 1'
    print(carrots)

def sameName2():
    carrots = 'carrots local 2'
    print(carrots)
    sameName1()
    print(carrots)

carrots = 'global'
sameName2()
print(carrots)

def spam():
    eggs = 99

    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
    print(eggs + ham)

spam()
bacon()

def spamEx():
    global rice
    rice = 'FDS'

rice = 'FDS-GRANDE'
spamEx()
print(rice)

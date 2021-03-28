def isPhoneNumber(text):
    if len(text)!=12:
        return False
    for i in range (0,3):
        #print("for")
        #print(i)
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range (4,7):
        #print("for")
        #print(i)
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range (8,12):
        #print("for")
        #print(i)
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number')
print(isPhoneNumber('Moshi moshi'))

print('\nWrite a message for the office')
message = input()

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone Number found:' + chunk)
print('Done')
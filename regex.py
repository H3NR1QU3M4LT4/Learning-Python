#\d qualquer digito de 0 a 9
#\D qualquer caracter que n seja digito de 0 a 9
#\w qualquer letra digito ou o caractere underscore
#\W qualquer caractere que não seja uma letra um digito ou caractere underscore
#\s qualquer espaço, tabulação ou caractere de quebra de linha
#\S qualquer caractere que n seja espaço, tabulação ou caractere de quebra de linha
#
#EXEMPLO
#\d+\s\w+ (textos que tenham um ou mais digitos-\d+-seguidos de um caractere
# de espaço-\s-seguido de um ou mais caracteres que sejam uma letra/digito
# ou underscore-\w+)
import re 

print('Write any message:')
message = input()
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall(message))

#[a-zA-Z0-9] todas as letras de 'a' a 'z' quer maiusculas quer minusculas
#e todos os numeros de 0 a 9

consoantRegex = re.compile(r'[^aeiouAEIOU]')
print(consoantRegex.findall(message))

#IDLE
beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello World!')
beginsWithHello.search('He said hello.') == None

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
endsWithNumber.search('Your number is two') == None

wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('12341234')
wholeStringIsNum.search('1234fds1234') == None

atRegex = re.compile(r'.at')
atRegex.findall('The car in the hat sat on fire on the flat mate.')

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
name = nameRegex.search('First Name: AI Last Name: Strong')
name.group(1)
name.group(2)

#greedy maior string é escolhida
#nongreedy menor string é escolhida
nongreedyRegex = re.compile(r'<.?>')
nongreedString = nongreedyRegex.search('<To serve man> for dinner.>')
nongreedString.group()

greedyRegex = re.compile(r'<.*>')
greedyString = greedyRegex.search('<To serve man> for dinner.>')
greedyString.group()

#pagina 205 revisão
import re

#IDLE
robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is bullshit!')
robocop.search('RoboCop is bullshit!').group()

namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret to Agent Bob, who is a bitch.')

agentNameRegex = re.compile(r'Agent (\w)\w*')
agentNameRegex.sub(r'\1****', 'Agent Alice who is dumb and Agent Bob fucked Agent Helen')

#página 207 apagar
# ? DAMN
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
#or
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # código de área
    (\s|-|\.)? # separador
    \d{3} # primeiros 3 dígitos
    (\s|-|\.) # separador
    \d{4} # últimos 4 dígitos
    (\s*(ext|x|ext.)\s*\d{2,5})? # extensão
    )''', re.VERBOSE)

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

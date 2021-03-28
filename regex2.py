import re

robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is bullshit!')
robocop.search('RoboCop is bullshit!').group()

namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret to Agent Bob, who is a bitch.')

agentNameRegex = re.compile(r'Agent (\w)\w*')
agentNameRegex.sub(r'\1****', 'Agent Alice who is dumb and Agent Bob fucked Agent Helen')


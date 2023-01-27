import re

#strong passwords
regexToMatch = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

mo = regexToMatch.search('99ASDa')

#print(mo.group())

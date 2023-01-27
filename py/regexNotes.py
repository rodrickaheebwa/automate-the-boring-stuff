import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())





#import re
#re.compile(r'')
#regex.search() - only first match
#regex.findall() - list of all matches/list of tuples of groups
#mo.group() - all groups
#mo.groups() - all groups stored in a tuple

#(), |, ?, *, +, {}, {}?, \d, \D, \w, \W, \s, \S, [], [^ ], ^, $, .,
#second re args - re.DOTALL, re.I or re.IGNORECASE
#regex.sub() - substitute match

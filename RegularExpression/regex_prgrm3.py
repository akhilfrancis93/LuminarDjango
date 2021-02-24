import re
#pattern="a+" #consecutive numbers
#pattern="a*"
#pattern="a{2}"
pattern="a{2,3}"
matcher=re.finditer(pattern,"aaaaaaabaaabaabaa _Z7K@")
for match in matcher:
    print(match.start())
    print(match.group())
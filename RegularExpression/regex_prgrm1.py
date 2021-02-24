#regular expression pattern match

import re
pattern="ab"

matcher=re.finditer(pattern,"abababbbbabab")
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print(count)


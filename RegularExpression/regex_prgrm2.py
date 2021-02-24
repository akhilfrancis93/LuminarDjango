import re

#pre defined character set
#pattern="[abc]"
#pattern="[A-Z]"
#pattern="[a-z]"
#pattern="[a-zA-Z]"
#pattern="[0-9]"
#pattern="[^a-zA-Z0-9]"

#predefined characters
#pattern="\s" #space
#pattern="\d" #[0-9]
#pattern="\D" #[^0-9]
#pattern="\w" #Except special charcters
#pattern="\W" #special characters

matcher=re.finditer(pattern,"abc _Z7K@")

for match in matcher:
    print(match.start())
    print(match.group())

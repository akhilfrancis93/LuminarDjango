import re
valid=[]
rule="[k][l]\d{2}\w\d{4}"
f=open("vehiclenumbers","r")
for numbers in f:
    number=numbers.rstrip("\n")
    matcher=re.fullmatch(rule,number)
    if matcher!=None:
        valid.append(number)
print(valid)


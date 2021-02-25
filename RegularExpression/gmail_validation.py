import re
rule="\w+@gmail.com"
gmail=input("enter mail")
matcher=re.fullmatch(rule,gmail)
if matcher==None:
    print("not valid")
else:
    print("valid")
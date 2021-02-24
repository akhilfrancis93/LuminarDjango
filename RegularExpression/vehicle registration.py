import re
rule="[K][L][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9][0-9]"

vehicle_number=input("enter vehicle number")

matcher=re.fullmatch(rule,vehicle_number)

if matcher==None:
    print("invalid")
else:
    print("valid")
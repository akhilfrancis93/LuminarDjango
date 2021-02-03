arr=[10,11,12,13,14,15,16,18]
element=int(input("enter element"))
flag=0
for i in arr:
    if element==i:
        flag=1
        break
    else:
        flag=0
if flag==1:
    print("element found")
else:
    print("element not found")

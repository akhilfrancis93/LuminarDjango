num1=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number"))

if(num1>num2)&(num1>num3):
    print("num1")
if(num2>num3):
    print("num2")
else:
    print("num3")
if(num2>num1)&(num2>num3):
    print("num2")
if(num1>num3):
    print("num1")

else:
    print("num3")
if(num3>num2)&(num3>num1):
    print("num3")
if(num3>num2):
    print("num2")
else:
    print("num1")


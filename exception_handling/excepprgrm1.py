num1=int(input("enter num1"))
num2=int(input("enter num2"))

try:
    res=num1/num2
    print(res)
except Exception as e:
    num2=int(input("enetr num2"))
    print(e.args)
finally:
    print("database transaction")
    print("file operation")
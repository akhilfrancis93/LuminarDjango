def sub_smart(fun):
    def inner(num1,num2):
        if num1<num2:
            (num1,num2)=(num2,num1)
        return fun(num1,num2)
    return

@sub_smart
def sub(num1,num2):

    return num1-num2
print(10,20)
lst=[1,2,3,4,5,6]
output=[num**2 for num in lst]
print(output)

#find even numbers
even=[num for num in lst if num%2==0]
print(even)

#common elements lst
lst=[1,2,3]
lst2=[3,4,5]

commonelements=[num1 for num1 in lst for num2 in lst2 if num1==num2]
print(commonelements)

#pair

lst=[1,2,3]
lst2=[4,5,6]

pair=[(num1,num2) for num1 in lst for num2 in lst2]
print(pair)

#remove list

lst1=[[10,20],[30,40],[50,60]]

op=[num for lst in lst1 for num in lst]
print(op)


#greater than 5

lst=[4,3,2,5,6,7,8]

op=[num-1 if num<5 else num+1 if num>5 else 5 for num in lst]
print(op)
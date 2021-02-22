lst=[4,6,8,9,3,2]

numbers=list(map(lambda num:num-1 if num<5 else num+1,lst))
print(numbers)
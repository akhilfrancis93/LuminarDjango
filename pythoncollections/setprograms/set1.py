#lst=[10,20,30,30,40,40]
#st=set(lst)
#print(st)

lst=[1,2,3,4]
num=5
st=set(lst)
for no in lst:
    res=num-no
    if res in st:
        print(no,res)
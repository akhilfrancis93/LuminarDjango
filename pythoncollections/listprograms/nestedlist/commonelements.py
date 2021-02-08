lst=[10,11,12,13,14]
lst1=[5,8,9,10,11,15,16]
nlist=[]
for i in lst:
    for j in lst1:
        if i==j:
            nlist.append(i)
        elif i>j:
            j+=1
        elif i<j:
            i+=1
print(nlist)

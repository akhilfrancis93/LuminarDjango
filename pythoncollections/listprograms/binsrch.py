arr=[3,4,2,1,8,7,6]
element=int(input("enter element"))
arr.sort()
low=0
upp=len(arr)-1
flag=0
while (low<=upp):

    mid=(low+upp)//2
    if element>arr[mid]:
        low=mid+1
    elif element<arr[mid]:
        upp=mid-1
    elif element==arr[mid]:
        flag=1
        break
if flag==0:
    print("element not found")
else:
    print("element found")





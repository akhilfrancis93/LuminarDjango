pattern="AABBC"
dict={}
for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        dict[ch]+=1
print(dict)

for key,value in dict.items():
    if value==1:
        print(key,"non recursive")
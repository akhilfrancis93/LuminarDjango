text="hello hai hello hai how are"
words=text.split(" ")
dict={}
for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
data=sorted(dict,key=dict.get,reverse=True)
print(data)
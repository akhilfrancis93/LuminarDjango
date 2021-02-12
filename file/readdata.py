f=open("demo","r")
dict={}
stopwords=["the","where","is","have","with","that","had","if","a","to","and","by"]
for lines in f:
    words=lines.rstrip("\n").split(" ")
    for word in words:
        if word in stopwords:
            pass
        else:
            if word not in dict:
                dict[word]=1
            else:
                dict[word]+=1
print(dict)
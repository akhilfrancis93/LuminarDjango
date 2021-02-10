f=open("demo","r")
name=set()
for lines in f:
    words=lines.rstrip("\n").split(" ")
    for word in words:
        name.add(word)
for word in name:
    print(word)
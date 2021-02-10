text="ABABAC"
dict={}
for ch in text:
    if ch not in dict:
        dict[ch]=1
    else:
        print(ch,"first recursive character")
        break


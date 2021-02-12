f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    confirmed_cases=data[-1]
    if state not in dict:
        dict[state]=int(confirmed_cases)
    else:
        dict[state]=int(confirmed_cases)
for k,v in dict.items():
    print(k," ",v)
print("highest:\n",max(dict,key=dict.get))
print("lowest:\n",min(dict,key=dict.get))
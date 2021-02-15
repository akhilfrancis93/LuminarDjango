f=open("movies.csv,"r")
dict={}

for lines in f:
    data=lines.rstrip("\n"),(",")
    movies=data[2]
    if movies not in dict:

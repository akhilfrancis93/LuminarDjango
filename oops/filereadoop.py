class employee:
    def __init__(self,id,name,desig,exp,sal):
        self.id=id
        self.name=name
        self.desig=desig
        self.exp=exp
        self.sal=sal
    def __str__(self):
        return self.name
emplst=[]

f=open("employees","r")
for lines in f:
    id,name,desig,exp,sal=lines.rstrip("\n").split(",")
    emplst.append(employee(id,name,desig,exp,sal))

#print employee whose designation developer

developer=list(filter(lambda emp:emp.desig=="developer",emplst))
for emp in developer:
    print(emp)
highsal=max(map(lambda emp:emp.sal,emplst))
print(highsal)

minsal=min(map(lambda emp:emp.sal,emplst))
print(minsal)

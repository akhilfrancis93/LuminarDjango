class Student:
    def __init__(self,role,name,course,total):
        self.role=role
        self.name=name
        self.course=course
        self.total=total

st=Student(100,"akhil","mca",200)
st1=Student(101,"ajay","bca",250)
st2=Student(102,"anu","mca",300)
st3=Student(103,"arun","bca",430)
students=[]
students.append(st)
students.append(st1)
students.append(st2)
students.append(st3)

#for student in students:
    #if student.course=="mca":
        #print(student.name)

mark=[]
for student in students:
    mark.append(student.total)
print(max(mark))
class Student:
    def __init__(self, role, name, course, total):
        self.role=role
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name

st=Student(100,"akhil","mca",200)
st1=Student(101,"ajay","bca",250)
st2=Student(102,"anu","mca",300)
st3=Student(103,"arun","bca",430)
student=[]
student.append(st)
student.append(st1)
student.append(st2)
student.append(st3)

res=list(map(lambda stud:stud.name.upper(),student))
print(res)

marks=list(map(lambda st:st.total+50,student))
print(marks)

mcastud=list(filter(lambda stud:stud.course=="mca",student))
for stud in mcastud:
    print(stud)


#chain

mcastude=list(map(lambda st:st.name,list(filter(lambda st:st.course=="mca",student))))
print(mcastude)

#maximum

marks=max(list(map(lambda st:st.total,student)))
print(marks)

#minimum

marks=min(list(map(lambda st:st.total,student)))
print(marks)
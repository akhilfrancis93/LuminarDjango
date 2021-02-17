class Student:
    cname="CMS"
    def __init__(self,rol,name):
        self.rol=rol
        self.name=name

    def print_student(self):
        print(self.rol)
        print(self.name)

ob=Student(100,"akhil")
ob.print_student()

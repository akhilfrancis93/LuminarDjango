class Parent:
    def phone(self):
        print("nokia")

class Child(Parent):
    def phone(self):
        print("samsung")
class Subchild(Child,Parent):
    def m3(self):
        print("inside subchild")

sb=Subchild()
sb.m3()



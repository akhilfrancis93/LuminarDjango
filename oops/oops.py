#object oriented programmming

class Person:
    def set_values(self,age,name):
        self.age=age
        self.name=name
    def print_values(self):
        print(self.age)
        print(self.name)

#object

obj=Person()
obj.set_values(25,"ajay")
obj.print_values()

obj1=Person()
obj1.set_values(24,"vijay")
obj1.print_values()


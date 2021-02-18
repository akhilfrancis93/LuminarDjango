class Math:
    def add(self):
        print("inside nop arg matheod")
    def add(self,num1):
        print("inside 1 arg method")
    def add(self,num1,num2):
        print("inside 2 arg method")

math=Math()
math.add(10,20)
#math.add(10)
#math.add()
#recently added method
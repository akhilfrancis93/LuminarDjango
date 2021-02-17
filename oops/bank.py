class Bank:
    def create_customer(self,acno,name,mab):
        self.acno=acno
        self.name=name
        self.mab=mab
    def deposit(self,amount):
        self.mab+=amount
        print("account credited with",amount,"avail balance",self.mab)
    def withdraw(self,amount):
        if amount>self.mab:
            print("insufficient balance")
        else:
            self.mab-=amount
            print("account debited with",amount,"avail balance",self.mab)

ob=Bank()
ob.create_customer(1000,"ajay",3000)
ob.deposit(5000)
ob.withdraw(10000)



class Employee:
    apply_raise=1.5
    def __init__(self,first,last,empid,pay):
        self.first=first
        self.last=last
        self.empid=empid
        self.pay=pay
    def display(self):
        print(f"{self.first} , {self.last} , {self.empid} , {self.pay} ")
    def pay_raise(self):
        self.payme = self.pay*self.apply_raise
        print(f"{self.payme} Employee {self.first}")
class Developer(Employee):
    def pay_raise(self):
        self.apply_raise=2.5
        self.payme = self.pay*self.apply_raise
        print(f"{self.payme} Developer {self.first}")
class Manager(Employee):
    def pay_raise(self):
        self.apply_raise=3.5
        self.payme = self.pay*self.apply_raise
        print(f"{self.payme} Manager {self.first}")
e1=Employee("Sachin","Tendulkar",10229,20000)
e2=Manager("Akash","DL",19829,10000)
e3=Developer("Ajay","Devgan",101762,25000)
e1.display()
e2.display()
e3.display()
e1.pay_raise()
e2.pay_raise()
e3.pay_raise()
d = {}
class Employee:
    def accept(self):
        self.name = input("Enter name:")
        self.address = input("Enter address:")
        self.pan = input("Enter pan:")
        self.basic = int(input("Enter basic salary:"))
        self.da = self.basic * 0.12
        self.deduction = self.basic * 0.13
        self.hra = self.basic * 0.15
        self.gross = self.basic + self.da + self.hra
        self.net = self.gross - self.deduction
        d.update({self.name:{"Name":self.name,"Address":self.address,"PAN":self.pan,"Basic Salary":self.basic,"DA":self.da,"HRA":self.hra,"Gross Salary":self.gross,"Net Salary":self.net}})
    def search(self):
        c = 0
        n = input("Enter employee name:")
        for i in d:
            if i == n:
                print("Employee found;")
                c = 1
                print(n, d[i])
        if c == 0:
            print("Employee not found;")
emp = Employee()

while True:
    print("1.Add Employee details \n2.Search Employee by name \n3.Print Employee details \n0.Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 1:
        emp.accept()
    elif ch == 2:
        emp.search()
    elif ch == 3:
        for key in d:
            print(key, d[key])
    else:
        break
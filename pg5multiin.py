class student:
        def __init__(self):
                self.name=input("enter name")
                self.age=int(input("enter age"))
        def display(self):
                print("name:",self.name)
                print("age:",self.age)
class derived(student):
        def __init__(self):
                super().__init__()
                self.sem=int(input("enter sem"))
                self.sub1=int(input("Enter subject1 marks"))
                self.sub2=int(input("Enter subject2 marks"))
                self.sub3=int(input("Enter subject3 marks"))
                self.sub4=int(input("Enter subject4 marks"))
                self.sub5=int(input("Enter subject5 marks"))
                #self.display()
        def display(self):
                super().display()
                print("subject 1 marks:",self.sub1)
                print("subject 2 marks:",self.sub2)
                print("subject 3 marks:",self.sub3)
                print("subject 4 marks:",self.sub4)
                print("subject 5 marks:",self.sub5)
class percentage(derived):
        def __init__(self):
                super().__init__()
                self.sum1=self.sub1+self.sub2+self.sub3+self.sub4+self.sub5
                self.percent=(self.sum1/500)*100
                #self.display()
        def display(self):
                #super().display()
                print("percentage is:",self.percent)
while True:
        print("1.details\n 2.percentage")
        ch=int(input("enter choice"))
        if ch==1:
                det=derived()
                det.display()
        elif ch==2:
                perc=percentage()
                perc.display()
        else:
                break



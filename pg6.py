class Person:
    #def _init_(self):
    def Hello(self,name=None,age=None):
        self.name=name
        self.age=age
        if name != None and age != None:
            print("Hello:",name)
            print("Your Age:",age)
        elif name != None:
            print("Hello:",name)
        else:
            print("Hello")
p = Person()
print("0 parameter passing")
p.Hello()
print("1 parameter passing")
p.Hello("ABC")
print("2 parameter passing")
p.Hello("ABC",24)

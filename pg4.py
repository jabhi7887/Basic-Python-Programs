class Operator:
    def __init__(self):
        self.l = []
    def accept(self, n):
        print("Enter integer elements;")
        for i in range(n):
            ele = int(input(f"Element {i+1}:"))
            self.l.append(ele)
        print("List = ", self.l)
    def __add__(self, other):
        nl = []
        for i in range(len(self.l)):
            nl.append(self.l[i] + other.l[i])
        print("After addition:", nl)
    def __sub__(self, other):
        nl = []
        for i in range(len(self.l)):
            nl.append(self.l[i] - other.l[i])
        print("After subtraction:", nl)
    def __mul__(self, other):
        nl = []
        for i in range(len(self.l)):
            nl.append(self.l[i] * other.l[i])
        print("After subtraction:", nl)
    def __floordiv__(self, other):
        nl = []
        for i in range(len(self.l)):
            nl.append(self.l[i] // other.l[i])
        print("After subtraction:", nl)
    def __pow__(self, other):
        nl = []
        for i in range(len(self.l)):
            nl.append(self.l[i] ** other.l[i])
        print("After subtraction:", nl)
'''
__truediv__ -> a/b
__mod__ -> a%b
__lshift__ -> a<<b
__rshift__ -> a>>b
__and__ -> a&b
__or__ -> a|b
__xor__ -> a^b
'''
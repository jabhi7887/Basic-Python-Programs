from pg4 import *

ob1 = Operator()
ob2 = Operator()

n = int(input("Enter the length of list:"))
print("1st list--")
ob1.accept(n)
print("2nd list--")
ob2.accept(n)
print(" 1.addition \n 2.subtraction \n 3.mulitplication \n 4.division \n 5.power \n 0.exit")
while True:
    ch = int(input("Enter ur choice:"))
    if ch == 1:
        ob1 + ob2
    elif ch == 2:
        ob1 - ob2
    elif ch == 3:
        ob1 * ob2
    elif ch == 4:
        ob1 // ob2
    elif ch == 5:
        ob1 ** ob2
    else:
        break
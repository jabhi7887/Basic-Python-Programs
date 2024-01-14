while True:
        print("========MENU=========")
        print("1. ValueError \n 2. file not found error \n 3.type error \n 4.name error \n 5.io error")
        ch=int(input("Enter your choice"))

        if ch==1:
                try:
                        a=input("Enter a file name:")
                        b=input("Enter a mode:")
                        f=open(a,b)
                        print("Successfull")
                except ValueError:
                        print("Value error")

        elif ch==2:
                try:
                        a=input("Enter the file name:")
                        f=open(a,'r')
                        print("successfull")
                except FileNotFoundError:
                        print("file not found error")

        elif ch==3:
                try:
                        a=input("Enter the file name:")
                        f=open(a,'r','w')
                        print("Successfull")
                except TypeError:
                        print("TYPE ERROR")

        elif ch==4:
                try:
                        a=input("Enter the file name:")
                        f=opens(a,'r')
                        print("Successfull")
                except NameError:
                        print("Name eror:")
        elif ch==5:
                try:
                        a=input("Enter the file name:")
                        f=open(a,'r')
                        f.write("hi")
                        print("Successfull")
                except IOError:
                        print("Io error")

        else:
                print("Enter the valid choice")
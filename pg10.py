import time
def decorated(function):
    def wrapper(*args):
        st=time.time()
        print("The starting time is ",st)
        function(*args)
        et=time.time()
        print("The ending time is ",et)
        d=et-st
        fname=function.__name__
        print(f"{fname} took {d} seconds to execute")
    return wrapper
def fibonacci():
    a,b=0,1
    while(1):
        yield a
        a,b=b,a+b
n=int(input("Enter the number upto which you want to generate the fibonacci "))
@decorated
def fib():
    f=fibonacci()
    for i in range(n+1):
        print(next(f))
if "__main__":
    fib()
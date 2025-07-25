#Fibonacci series

def fibonacci_series(num):
    a=1
    b=0
    for i in range (1,num+1):
        c=a+b
        print(c)
        a=b
        b=c
num=int(input(" Enter a number:"))
print(fibonacci_series(num))
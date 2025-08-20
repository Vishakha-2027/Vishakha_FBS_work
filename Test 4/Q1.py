# write a function to which  we pass a parameter and print the factorial og a given number.for eg: factrors of 12:1,2,3,4,6,12
def fact(n):
    fact=1
    for i in range(1,n+1):
     if(n%i==0):
        print(i)
n=int(input("Enter a number"))
fact(n)
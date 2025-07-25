#a

def series(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total

num=int(input("Enter a positive integer:"))
result=series(num)
print(" The sum of series is:",result)


#b

def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
def sum_factorial(n):
    total=0
    for i in range(1,n+1):
        total+=fact(i)
    return total
n=int(input(" Enter n:"))
print(" sum is factorial mo is:",sum_factorial(n))



def power(num):
    total=0
    
    for i in range(1,num+1):
        total=i**i
        print(total)

num= int(input(" Enter n:"))
print(" sum of power series",power(num))


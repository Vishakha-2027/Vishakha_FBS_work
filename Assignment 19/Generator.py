# 1. Fibonacci generator
def fib_gen(limit):
    a,b=0,1
    while a <= limit :
        yield a
        a,b =b ,a+b
print("Fibonacci number up to 100:")
print(list(fib_gen(100)))

#2.Palindrome number generator
def palindrome_gen():
    num=0
    while True:
        if str(num)==str(num)[::-1]:
            yield num
        num +=1

pal =palindrome_gen()
print("First 10 Palindromes:",[next(pal)for _ in range(10)])


#3. Custom range generator
def my_range(start,stop,step=1):
    while start <stop:
        yield start
        start += step

print("my range 2 to 10 step 2:",list(my_range(2,10,2)))

#1. Memoization Decorator
def memoize(func):
    cache={}
    def wrapper(n):
        if n not in cache:
            cache[n]=func(n)
        return cache[n]
    return wrapper
@memoize
def factorial(n):
    if n==0 or n==1:
        return 1
    return n* factorial(n-1)

print("Factorial(5):",factorial(5))
print("Factorial(6):",factorial(6))
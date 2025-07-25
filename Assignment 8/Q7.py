#sum digit of a number

def sumOfdigit(num):
    total=0
    while(num>0):
        digit = num % 10
        total += digit
        num =num //10
    return total
n=int(input(" Enter a number:"))
print("sum of digit is:",sumOfdigit(n))
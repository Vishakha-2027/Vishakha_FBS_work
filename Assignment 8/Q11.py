#Armstrong number or not

def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = sum(int(digit)**power for digit in num_str)
    return total == n

num=int(input(" enter a number:"))
if is_armstrong(num):
    print("The number is  Armstrong number")
else:
    print(" The number is not  Armstrong number")
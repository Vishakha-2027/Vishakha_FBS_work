# reverse 3 digit no 

num = int(input("enter a digit"))
a = num % 10
num = num // 10
b = num % 10
reverse = (a * 10)+ b
c = num // 10
reverse = (reverse * 10)+ c
print(" the Reverse no is : " ,reverse)
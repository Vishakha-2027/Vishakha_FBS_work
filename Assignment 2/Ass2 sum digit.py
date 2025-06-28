#sum of digit in 3 digit no

num = int(input(" enter of digit:"))
a = num % 10
num = num //10
c = num % 10
d = num // 10
sum = a+c+d


print = (" Sum of 3 digit is :" ,sum)
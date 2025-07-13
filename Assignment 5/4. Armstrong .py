num = int(input(" Enter a number to check if its an Armstrong number:"))
temp = num
order = len(str(num))
sum_armstrong = 0

while temp > 0:
    digit = temp % 10
    sum_armstrong += digit ** order 
    temp//=10

if  sum_armstrong == num :
    print(" is an Armstrong number",num)
else:
    print("is not an Armstrong number", num)

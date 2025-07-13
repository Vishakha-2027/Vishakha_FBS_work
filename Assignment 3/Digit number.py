num = int(input(" Enter a 3 digit number:"))
copy = num

a= num%10
num=num//10
b=num%10
reverse=(a*10)+b
c=num//10
reverse=(reverse*10)+c

if(copy==reverse):
    print(" The enter a 3digit num is palindrom")
else:
    print("The enter a 3digit num is no palindrom")
    
num = int(input("Enter a three digit no.:"))

First = (num // 100)
Second =(num //10 )%10
three = (num %10)

if (First == 2* Second and First / three== 2):
    print("Yes you have done it")
else:
    print(" Please try next time")

def SumOfDigit(num):
    if(num==0):
        return 0
    else:
        a= num%10
        return a+SumOfDigit(num//10)
    
num=int(input("enter a number"))
print(SumOfDigit(num))
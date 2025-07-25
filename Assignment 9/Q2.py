def count(num):
    if(num !=0):
        return 1+count(num//10)
    else:
        return 0
    
def armstrong(num,c):
    if num==0:
        return 0
    else:
        return(num%10)**c+ armstrong (num//10,c)
    
num=int(input(" Enter a number:"))
c=count(num)
ams=armstrong(num,c)

if ams==num:
    print(num," is an armstrong number")
else:
    print(num," is not an armstrong number")
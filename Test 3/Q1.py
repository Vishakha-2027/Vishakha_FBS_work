# write a program to print first n prime number

num=int(input(" Enter a number:"))
for num in range(2,num+1):
    for i in range(2,num):
        if(num% i==0):
            
            break
    else:
        print(num)
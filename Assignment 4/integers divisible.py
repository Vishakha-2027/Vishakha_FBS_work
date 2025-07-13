integers = int(input(" Enter the  integers number:"))

for i in range (1,integers+1):
    if(i % 2 != 0)and (i % 3 !=0):
        print(i)
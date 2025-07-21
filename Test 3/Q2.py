#1/1! +2/2!+ 3/3!+4/4!+........N/N!

num= int(input(" Enter a number:"))
sum=0
for i in range(1,num+1):
    fact=1
    for j in range (1,i+1):
        fact= fact*j
        sum += i / fact
    print(fact)
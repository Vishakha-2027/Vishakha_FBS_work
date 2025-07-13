start = int(input(" Enter a start number:"))
stop = int(input(" Enter a stop number :"))
print(" The number which are divisible by 7 and multiply by 5 are:")

for i in range (start,stop):
    if(i%7==0 and i %5 ==0 ):
        print(i)
start =  int(input(" Enter a start number:"))
stop = int(input(" Enter a stop number:"))

for i in range(start,stop+1):
    temp =i
    count=0
    while(temp !=0):
        count +=1
        temp = temp//10
    temp = i
    sum = 0

    while(temp !=0):
        a = temp %10
        sum += a** count
        temp = temp//10
    if(sum==i):
     print(i,"yes it is armstrong")
num = int(input("Enter a number:"))
divisior = 0

for i in range(1,num):
    if(num %i == 0):
        divisior += i
if (divisior == num):
    print("The perfect a number ")
else:
    print(" It is not a perfect number")
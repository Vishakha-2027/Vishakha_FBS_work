num = int(input("Enter a number:"))

for i in range (2,num):
    if(num%2==0):
        print("Not prime")
        break
else:
    print(" prime")
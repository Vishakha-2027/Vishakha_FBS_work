num = int(input(" enter a number:"))

for i in range (2, num ):
    if (num % 2 ==0):
        print ("Not prime number")
        break
else:
    print(" the prime number")
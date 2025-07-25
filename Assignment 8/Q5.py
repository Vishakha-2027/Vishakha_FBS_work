# sum of prime numbers

def prime(num):
    sum=0
    for num in range(2,num+1):
        for i in range(2,num):
            if (num%i==0):
                break
        else:
            sum=sum+num
    return sum

num=int(input(" Enter the number:"))
print(prime(num))



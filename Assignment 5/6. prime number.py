


num = 2
while num <= 100:
    is_prime = True 
    i =2
    while i * i <= num:
        if  num %i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num , end=" ")
    num += 1


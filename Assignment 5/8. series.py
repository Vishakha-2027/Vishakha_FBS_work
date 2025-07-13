#a

n = int(input(" Enter value of n:"))
i = 1
sum_series = 0

while i <= n:
    fact = 1
    j = 1
    while j <= i :
        fact *= j
        j += 1
    sum_series += fact
    i += 1

    print (" sum of factorial series:" , sum_series)


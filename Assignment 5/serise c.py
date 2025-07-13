#8.c
n = int(input(" Enter the number of n:"))

i = 0
sum_series = 0

while i < n:
        term = 2 ** i
        sum_series += term
        i += 1
        
print(" Sum  of the series 1 + 2 + 4 + ..." , n  ,(" terms=" ) ,sum_series)

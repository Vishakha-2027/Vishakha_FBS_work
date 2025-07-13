#8 .b


N = int(input(" Enter the value of n:"))
i = 1
sum_series = 0
while i <= N:
        sum_series += N ** i
        i += 1
        
        
print(" Sum of the series N + N^2 + N^3 +...+N^N" , sum_series)
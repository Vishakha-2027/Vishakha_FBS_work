x = float(input(" Enter the value of x:"))
n = int(input(" Enter number of terms:"))

i = 1
denominator = 1
sign = 1
sum_series = 0

while i <= n :
    term = sign *(x ** i)/denominator
    sum_series += term

    sign *=  -1
    denominator += 2
    i += 1
print(" Sum of the series =" ,sum_series)
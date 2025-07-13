a = float(input(" Enter the value of a:"))

i = 1
sum_series = 0

while i <= 10 :
    term = (a ** i)/i
    sum_series += term
    i +=1

print("Sum  of the series S = a + a^2/2 + a^3/3 +....+a^10/10 is :" , sum_series)
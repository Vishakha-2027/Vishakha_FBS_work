start = int(input(" Enter the strat of range:"))
end = int(input(" Enter the end of the range:"))

divisor = int(input(" Enter the number to divide :"))

for i in range (start , end+1):
    if (i % divisor == 0):
        print(i)
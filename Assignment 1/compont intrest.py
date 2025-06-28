# find compont intrest

p = int(input("enter the principal amount:"))
t = int (input("enter the timein year:"))
r = int (input("enter the rate:"))

CI = p*((1+r/100)**t)
print("the compont intrest is:",CI)
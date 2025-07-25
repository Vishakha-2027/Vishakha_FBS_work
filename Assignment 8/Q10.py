#leap year or not

def is_leap_year(year):
    return(year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0)
yr = int(input("Enter a year:"))
if is_leap_year(yr):
    print(" It's a leap year")
else:
    print("it's not a leap year")
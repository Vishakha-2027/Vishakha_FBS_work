year = int(input("Enter a year:"))

if (year % 4 !=0):
    print("not the leap year")
elif (year % 100!=0):
    print(" The leap yera")
elif( year%400!=0):
    print(" not leap year")
else:
    print("The leap year")
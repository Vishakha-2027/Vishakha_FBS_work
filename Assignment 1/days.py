#to find years ,week,and days from given no.of days

days = int(input(" enter no.of days:"))
years = days//365
days = days%365            #we calculate remaning days
weeks = days//7
days = days%7

print("years:",years)
print("weeks:",weeks)
print("days:",days)
# program to calculate total salary based on componet

basic = float(input(" Enter Basic Salary:"))

# calculation allowances
da = 0.10 * basic
ta = 0.12 * basic 
hra = 0.15 * basic

#Total salary
total_salary = basic+da+ta+hra

print(" Basic Salary:",basic)
print("DA(10% :" ,da)
print("TA(12%):",ta)
print("HRA(150%):",hra)
print(" Total Salary:",total_salary)
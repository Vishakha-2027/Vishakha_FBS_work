marks= int(input("enter marks subject 1:"))
marks= int(input("enter marks subject 2:"))
marks= int(input("enter marks subject 3:"))
marks= int(input("enter marks subject 4:"))
marks= int(input("enter marks subject 5:"))
for i in range(1,6):
    m= float(input(" enter marks for subject (i):"))
    marks.append(m)


total= sum(marks)
percentage= total/5

print(" Total Marks:",total)
print("Percentage:" , percentage)

if (percentage>=60):
    print("Grade:First Class")
elif (percentage>=50):
    print("Grade: Second Class")
elif(percentage>=35):
    print("Grade:Pass Class")
else:
    print("Grade:Fail")
a = float(input("Enter length of side a:"))
b = float(input("Enter length of side b:"))
c = float(input("Enter length of side c:"))

if(a+b>c)and (a+c>b) and(b+c>a):
    if(a==b==c):
        print(" The triangle is Equilateral")
    elif(a==b)or(b==c)or(a==c):
         print("The triangle is Isoscles")
    else:
       print("The triangle is Scalene")
else:
    print("The given sides do not form a valid triangle")

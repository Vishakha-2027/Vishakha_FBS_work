side1 = float(input(" Enter first side of the triangle:"))
side2 = float(input(" Enter second side of the triangle:"))
side3 = float(input(" Enter third side of the triangle:"))

if(side1 + side2 > side3 )and (side1+side3>side2) and (side2+side3>side1):
    print("The triangle is vaild")

else:
    print(" The triangle is not vaild")
    
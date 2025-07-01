# WAP to find the area and perimeter of following fig.(accept the length,breadth and radius )

length = float(input(" Enter length of the rectangle:"))
breadth = float (input(" enter breadth of the rectangle:"))
radius = float(input(" Enter the radius of the semicircle:"))

renctangle_area = length* breadth
semicircle_area = 0.5 * 3.14 * radius ** 2
total_area = renctangle_area + semicircle_area

perimeter = length + (2 * breadth) + (3.14 * radius)

print (" Area of the figure:", total_area)
print (" Perimeter :" , perimeter)



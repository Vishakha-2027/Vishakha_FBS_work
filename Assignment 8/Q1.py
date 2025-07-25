#calculate area of rectangle

def area_renctangle(length,width):
    return length * width

l=int(input(" Enter the length of the renctangle:"))
w=int(input("Enter the width of the renctangle:"))

area= area_renctangle(l,w)
print("Area of the renctangle is:",area)
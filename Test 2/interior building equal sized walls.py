height = float(input("Enter a hight of wall:"))
width = float(input(" Enter width of wall:"))
cost_sqm = 10

if(height>0 and width>0):
    area_one_wall = height*width
    total_area = area_one_wall*4
    total_cost = total_area*cost_sqm
    print(" total cost of paintaing 4 walls is rs",total_cost)

elif(height<=0 and width<0):
    print("Hight and width must me greater than 0")

elif(height<=0):
    print("Height must be grater than 0")

elif(width<=0):
    print(" Width must be greater than 0")

else:
    print(" Invalid output")
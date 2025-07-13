radius = 20
length = 50
breadth = 40
cost_per_meter = 35
layers = 5

if(radius>0 and length>0 and breadth>0 and cost_per_meter>0 and layers>0):
    half_circle = 3.14*radius
    rectangle =  2 * length +breadth
    total_length = (half_circle+rectangle)*layers
    total_cost = total_length*cost_per_meter
    print(" Total cost of fencing is Rs",total_cost)
else:
    print(" Invalid input")
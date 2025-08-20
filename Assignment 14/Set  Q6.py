numbers =[3,5,7,2,8,10]

max_product=float('-inf')
pair=()

for x in numbers:
    for y in numbers:
        if x !=y and x*y > max_product:
            max_product = x*y
            pair = (x,y)
print("Two numbers:",pair,"max product",max_product)
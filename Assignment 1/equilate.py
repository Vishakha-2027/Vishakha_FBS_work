# find roots of a quadraric equation

a = int (input(" enter a:"))
b = int (input(" enter b:"))
c = int (input(" enter c :"))

ans = (b*b)- (4*a*c)
ans = ans ** 0.5
root1 = (-b+ ans)/(2*a)
root2 = (-b- ans)/(2*a)
print(" Root1:",root1)
print ("Root2:",root2)
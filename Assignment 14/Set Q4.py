number=list(map(int,input("enter a number:").split()))
target=int(input("enter a target sum"))
pairs=set()
for i in range (len(number)):
    for j in range(i+1,len(number)):
        if number[i]+number[j]== target:
            pairs.add((number[i] ,number[j]))
print("pairs with sum",target,":",pairs)
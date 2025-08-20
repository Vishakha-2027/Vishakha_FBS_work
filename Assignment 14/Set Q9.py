from itertools import combinations
num=[1,2,3,4,5,6,7]
target=10

result=[combo for combo in combinations (num,3) if sum(combo) ==target]

print("combinations of 3 numbers with sum",target,":",result)
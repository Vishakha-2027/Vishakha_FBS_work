dict1={1:"A" ,2:"B"}
dict2={3:"c",4:"D"}

for key in dict2:
    dict1[key]= dict2[key]

print("concatenated dictionary:",dict1)
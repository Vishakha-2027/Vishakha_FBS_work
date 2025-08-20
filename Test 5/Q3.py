data=[[101,"seema",45000],[340,"Rajani",13000],[210,"Tannu",14000],[320,"suresh",35000]]
sorted_data=sorted(data,key=lambda x:x[2])
print("Sorted by salary:")
for emp in sorted_data:
    print(emp)
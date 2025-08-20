n=int(input("enter number of element in the list:"))

input_list=[]
print("enter the string element:")
for i in range(n):
    element=input(f"element{i+1}:")
    input_list.append(element)
sorted_list=sorted(input_list,key=len)
print("original list:",input_list)
print("sorted list by lenghth:",sorted_list)
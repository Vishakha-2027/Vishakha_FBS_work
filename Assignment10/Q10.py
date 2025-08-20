list1=[1,2,67,56,34,78,56]
ele=int(input("Enter a element"))
c=0
for i in range(len(list1)):
    if (ele == list1[i]):
        c+=1
for i in range(c):
    list1.remove(ele)
print(list1)
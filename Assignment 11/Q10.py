#print list after removing even numbers

list1=[12,23,34,44,45,67,78]
list2=[]
for i in (list1):
    if (i%2==0):
        list2.append(i)
print(list2)
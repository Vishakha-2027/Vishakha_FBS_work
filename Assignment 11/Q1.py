#even and odd element into 2 diff list

list1=[2,3,4,5,6,7,8,9,10]
even_list=[]
odd_list=[]
for i in list1:
    if(i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)
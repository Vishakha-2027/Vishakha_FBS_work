list1=[12,7,6,15,8]
list2=[]
for i in list1:
  if(i%2!=0) :
    list2.append(list1)

print("orignal list",list1)
print('list after removing even no ',list2)
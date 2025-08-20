list1=[11,22,56,22,67,89]
new_lst=[]
for i in list1:
    if i not in new_lst:
        new_lst.append(i)
print("Without duplicates",new_lst)
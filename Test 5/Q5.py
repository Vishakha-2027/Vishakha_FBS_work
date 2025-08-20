def union_lists(list1,list2):
    union=list1[:]
    for item in list2:
        if item not in union:
            union.append(item)
    return union
list1=[1,2,3,4]
list2=[3,4,5,6]
print("union:",union_lists(list1,list2))
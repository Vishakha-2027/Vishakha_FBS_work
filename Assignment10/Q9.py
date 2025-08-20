list1=[2,3,5,8,9,23]
even=[]
odd =[]
for i in list1:
    if i % 2 ==0 :
        even.append(i)
    else:
        odd.append(i)
print("Even list:",even)
print("odd list:",odd)
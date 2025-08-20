# find 2nd largest number using bubble sort

list1=[54,67,76,43,98]
list2=len(list1)

for i in range(list2):
    for j in range(0,list2-i-1):
        if(list1[j] > list1[j+1]):
            list1[j],list1[j+1]=list1[j+1],list1[j]
print("second largest number is:",list1[-2])
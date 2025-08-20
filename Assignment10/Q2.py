list1=[]
n=int(input("Enter a number element:"))

for i in range(n):
    marks=int(input("Enter a marks:"))
    list1.append(marks)
print("Given marks are",list1)
min_marks =min( list1)
max_marks = max(list1)
print(f'min:{min_marks},max:{max_marks}')

total=sum(list1)
n=len(list1)
print("Average:",total //n)
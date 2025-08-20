num=int(input("enter the no of element"))
list1=[]
for i in range(num):
    ele=int(input("Enter the element"))
    list1.append(ele)
print("list given by user",list1)

m=int(input("enter a first divisor"))
n=int(input("enter a second divisor"))
new_list=[]
for i in range(num):
    if(list1[i]% m==0 and list1[i]%n==0):
        new_list.append(list1[i])
print(new_list)
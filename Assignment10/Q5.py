list1=[24,36,84,10]
x=int(input("Enter a element:"))
for i in range(len(list1)):
    if (x==(list1[i])):
        print("Yes it is present")
        break
else:
    print(" Not it is present")
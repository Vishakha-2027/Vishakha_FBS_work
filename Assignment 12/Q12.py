str=input("enter a string")
count=0
for ch in str:
    if ch>='a'and ch <='z':
        count+=1
print("lowercase string",count)
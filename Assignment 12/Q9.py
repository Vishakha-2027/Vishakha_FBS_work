str=input("enter a string")
words=str.split()
num_word=len(words)
count_char=0
for ch in str:
    if ch!=" ":
        count_char+=1
print("number of words",num_word)
print("number of charecter:",count_char)
str=input("enter a string:")
words=str.split()
word_count={}

for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print("occurrence of each word:")
for word,count in word_count.items():
    print(word,":",count)
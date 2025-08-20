text="python is easy and python is powerful"
words=text.split()

freq={}

for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print("word frequency:",freq)

    
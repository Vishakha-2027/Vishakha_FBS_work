words=[" apple","banana","apple","orange","banana","apple"]
unique_words=set(words)
for words in unique_words:
    frequency ={words:words.count(words)}

print("Unique words:",unique_words)
print("frequency",frequency)
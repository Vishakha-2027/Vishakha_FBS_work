words=["eat","tea","tan","ate","nat","bat"]

anagrams={}
for word in words:
    key = ''.join(sorted(word))
    anagrams.setdefault(key,[]).append(word)
print("Grouped anagrams:",list(anagrams.values()))
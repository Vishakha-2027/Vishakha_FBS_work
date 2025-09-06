# 1. Numbers Divisible by 8
div_by_8=[x for x in range(1,1001) if x % 8 == 0]
print("Number divisible by 8 :", div_by_8)

#2. Number that have  digit 6
with_6=[x for x in range(1,1001)if '6' in str(x)]
print("Number containg 6 :",with_6)

# 3.count space in string
s="python is a  powerful programing language"
space_count=sum([1 for ch in s if ch == ' '])
print("Space:",space_count)

#4. Remove vowels
s="hello world python is awesome"
no_vowels=''.join([ch for ch in s if ch.lower() not in 'aeiou'])
print("Without vowel:",no_vowels)

#5.words less than 5 letters
sentence="python is fun and very powerful"
short_word=[word for word in sentence.split() if len (word)<5]
print("words less than 5 letters:",short_word)

#6. Dictionary comprehension -word lengths
sentence="python makes coding very easy"
word_len={word:len(word) for word in sentence.split()}
print("word lengths:",word_len)

#7. Nested comprehension _divisible by single digit
div_by_digit=[x for x in range(1,1001)if True in [x % d==0 for d in range(2,10)]]
print("Divisible by single digit:",div_by_digit)
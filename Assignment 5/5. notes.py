amount = int (input(" Enter the amount "))
notes = (2000, 500 , 200 , 100 , 50 , 20, 10 , 5 , 2 , 1)
i = 0
print(" Minimum number of notes needed:")

while i < len(notes):
    if amount >= notes [i]:
        count = amount // notes [i]
        amount %= notes[i]
        print( " The notes",  notes , count)
    i += 1
D=[2000,500,200,100,50,20,10,5]
def min_notes(amount):
    notes_used={}
    for note in D:
        if(amount>=note):
            count=amount//note
            notes_used[note]=count
            amount=amount%note
    return notes_used

amount=4855
result=min_notes(amount)
print("Notes used:",result)
print("minimum number of notes:",sum(result.values()))

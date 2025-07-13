num_passenger =int(input(" Enter number of passengers:"))
ticket_cost = float(input(" Enter ticket cost per passenger:"))

i = 0
total_amount = 0

while i< num_passenger:
    age = int(input(" Enter age of passenger",))
    
    if age < 12 :
        discount = 0.30
    elif age > 59 :
        discont = 0.50
    else:
        discont = 0.0

    final_cost = ticket_cost * (1- discount)
    total_amount += final_cost

    print(" Passenger pays" ,final_cost)
    i +=1

print(" Total amount to be paid for all passengers:")
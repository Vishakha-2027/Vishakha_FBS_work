correct_userid = "admin"
correct_password = " 1234"
attempt =0

while attempt <3:
    userid = input(" Enter user ID:")
    password = input(" Enter password:")

    if userid == correct_userid and password == correct_password:
        print(" Logic succefull")
        break
    else:
        print("Incorrect ID or password try again")
        attempt +=1
if attempt==3:
    print(" 3 attempt used access denied")

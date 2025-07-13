correct_userid=("admin")
correct_password=("12345")

entered_userid=input("Enter User ID:")
entered_password =input("Enter  Password:")

if(entered_userid== correct_userid )and (entered_password== correct_password):
    print("Login successfull")
else:
    print(" Invalid User ID or Password")
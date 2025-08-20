my_dict={"name":"kiran","age":22,"city":"pune"}

key_to_remove="age"
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
print("dictionary after remove:",my_dict)
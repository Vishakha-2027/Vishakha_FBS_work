p1 = float(input("Enter price of product 1:"))
p2 = float(input("Enter price of product 2:"))
p3 = float(input("Enter price of product 3:"))
p4 = float(input("Enter price of product 4:"))
p5 = float(input("Enter price of product 5:"))

total = p1+p2+p3+p4+p5

if(total>0):
    gst = total *0.18
    final_bill = total +gst
    print("Total",total)
    print("GST",gst)
    print("Total bill after adding 18%  gst is rs:",final_bill)
else:
    print("Invalid input")
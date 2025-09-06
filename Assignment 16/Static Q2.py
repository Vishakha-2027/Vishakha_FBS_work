#product Class

class Product:
    discount = 0.1 
    def __init__(self,pid=0,pname=" Unknown",price=0,quantity=0):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity
        
    def showProduct(self):
        print(f"Product ID:{self.pid},Name:{self.pname},Price:{self.price},Quantity:{self.quantity}")

    def applyDiscount(self):
        new_price=self.price -(self.price * Product.discount)
        print(f"Price after discount:{new_price}")

print("\n--- Product Class---")
p1=Product(101,"Laptop",50000,2)
p1.showProduct()
p1.applyDiscount()
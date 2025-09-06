# Shirt Class

class Shirt:
    size_price={"small":1.0,"medium":1.1,"large":1.2,"xlarge":1.3}
    def __init__(self,sid=0,sname=" Unknown",stype="Unknow",price=0,size="small"):
        self.sid=sid
        self.sname=sname
        self.stype= stype
        self.price = price
        self.size=size

    def showShirt(self):
        final_price =self.price * Shirt.size_price[self.size]
        print(f"Shirt ID:{self.sid},Name:{self.sname},Type:{self.stype},size:{self.size},Price:{final_price}")
         
print("\n-- Shirt Class---")
s1=Shirt(201,"Formal Shirt","Formal",1000,"medium")
s2=Shirt(202,"Casual Shirt","Casual",1000,"xlarge")
s1.showShirt()
s2.showShirt()
        

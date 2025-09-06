#Shirt class

class Shirt:
    def __init__(self,sid=None,sname=None,stype=None,price=None,size=None):
        self.sid=sid
        self.sname=sname
        self.price=price
        self.size=size
        self.stype=stype
        print("shirt object created")

    def showShirt(self):
        print("---shirt details---")
        print("shirt Id:",self.sid)
        print("shirt name:",self.sname)
        print("type:",self.stype)
        print("size:",self.size)
        print("------------------")

    def __del__(self):
        print("shirt object destroyed")

s1=Shirt()
s1.showShirt()

s2=Shirt(301,"peter england,""Formal",1200,"large")
s2.showShirt()
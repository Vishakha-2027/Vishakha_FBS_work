#Book class

class Book:
    def __init__(self,bid=None,bname=None, price=None,author=None):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
        print("Book object created !")

#Showbook method

def showBook(self):
    print("--- Book Details---")
    print(" Book ID",self.bid)
    print("Book Name",self.bname)
    print("price",self.price)
    print("author",self.author)
    print("---------------")

    #Destructor

    def __del__(self):
        print("Book object Destroyed")

b1=Book(101,"python programming",500,"guido van rossum")
b1.showBook()
del b1
    
    
    
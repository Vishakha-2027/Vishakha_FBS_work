class Book:
    count=0
    def __init__(self,bid=0,bname=" Unknown",price=0,author="Unknown"):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
        Book.count +=1

    def __del__(self):
        Book.count -=1

    def showBook(self):
        print(f"Book Id:{self.bid},Name:{self.bname},price:{self.price},author:{self.author}")

    @staticmethod
    def showCount():
        print("Total Book Objects:",Book.count)

print("\n --- Book Class ---")
b1=Book(1,"python",500,"Guido")
b2=Book(2,"DSA",600,"Mark")
b1.showBook()
b2.showBook()
Book.showCount()
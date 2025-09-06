class Television:
    def __init__(self):
        self.model_no=0
        self.screen_size =0
        self.price = 0

    def get_input(self):
        try:
            self.model_size=int(input("Enter number (max 4 digit):"))
            self.screen_size=int(input("Enter screen size (12 to 70 inches):"))
            self.price=int(input("Enter price(0-500 Rs):"))

            if self.model_no > 9999:
                raise ValueError("Model number should be at most 4 digits")
            
            if self.screen_size < 12 or self.screen_size > 70:
                raise ValueError("Screen size must be between 12 and 70 inches")
            
            if self.price < 0 or self.price > 5000 :
                raise ValueError("Price must be between 0 and 5000")
            
        except Exception as e:
            print("Error :",e)
            print("Resetting values to 0")
            self.model_no=0
            self.screen_size =0
            self.price = 0

    def display(self):
        print("\n Television Details :")
        print("Model Number :",self.model_no)
        print("Screen Size:",self.screen_size)
        print("Price :",self.price)

if __name__ =="__main__":
    tv = Television()
    tv.get_input()
    tv.display()
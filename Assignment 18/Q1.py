class Complex:
    #constructor
    def __init__(self,real=0,imag=0):
        self.real=real
        self.imag=imag
        print(f"Constructor called:{self.real}+{self.imag} i created")

     #destructor
    def __del__(self):
        print(f"Destructor called:{self.real}+{self.imag} i destroyed")

    def __str__(self):
        return f"{self.real}+{self.imag} i"
    
    def __add__(self,other):
        return Complex(self.real+other.real,self.imag+other.imag)
    
    def __sub__(self,other):
        return Complex(self.real-other.real,self.imag-other.imag)
    
c1 = Complex(3,2)
c2 = Complex(1,7)

print("c1=",c1)
print("c2=",c2)

c3=c1+c2
print("c1+c2=",c3)

c4 = c1-c2
print("c1-c2=",c4)

class Distance:
    def __init__(self,km=0,m=0,cm=0):
        self.km=km
        self.m=m
        self.cm=cm
        print(f"Constructur called:{self.km} km{self.m}m{self.cm} cm created")
        

    def __del__(self):
        print(f"Destructor called:{self.km}km{self.m}m{self.cm}cm destroyed")

    def __str__(self):
        return f"{self.km}km{self.m}m{self.cm}cm"
    
    def normalize(self):
        self.m +=self.cm//100
        self.cm = self.cm %100
        self.km += self.m //1000
        self.m = self.m%1000

    def __add__(self,other):
        d=Distance(self.km + other.km, self.m+other.m,self.cm+other.cm)
        d.normalize()
        return d
    def __sub__(self,other):
        d=Distance(self.km - other.km, self.m-other.m,self.cm-other.cm)
        d.normalize()
        return d
    
d1=Distance(2,300,50)
d2= Distance(1,800,80)
print("d1=",d1)
print("d2=",d2)

d3=d1+d2
print("d1+d2=",d3)

d4 = d1-d2
print("d1-d2=",d4)
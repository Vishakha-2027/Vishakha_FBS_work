class Student:
   def __init__(self,student_id,name,age,percentage):
      self.student_id = student_id
      self.name = name
      self.age=age
      self.percentage = percentage

   def display(self):
      print( f"ID:{self.student_id},Name:{self.name},age:{self.age},Percentage:{self.percentage}")

   def accept(self):
      self.student_id=input("Enter Student Id:")
      self.name=input("Enter Name")
      self.age=int(input("enter age:"))
      self.percentage=float(input("Enter percentage:"))
    
   def calculate_rank(self):
      if self.percentage >= 85:
         return "A"
      elif self.percentage >= 70:
          return "B"
      elif self.percentage >= 50:
          return "C"
      else:
         return "D"
      
   def __str__ (self) :
      return f"student({self.student_id},{self.name},{self.age},{self.percentage},Rank:{self.calculate_rank()})"
   
if __name__ == "__main__":
   s1=Student("S101","Rahul",20,82)
   s1.display()
   print("Rank:",s1.calculate_rank())
   print(s1)
    
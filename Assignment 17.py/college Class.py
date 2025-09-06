from enggStudent import EnggStudent
from medicalStudent import MedicalStudent
from student import Student
#college class

class College:
 def __init__ (self,max_students):
  self.max_students=max_students
  self.students=[]

 def add_student(self,student):
  if len(self.students)< self.max_students:
    self.students.append(student)
  else:
   print("College if full ! Cannot add more students.")

 def get_student(self,student_id):
  for s in self.students:
   if s.student_id ==student_id:
     return s
  return None
  
 def remove_student(self,student_id):
   self.students=[s for s in self.students if s.student_id != student_id]

 def __str__(self):
     if not self.students:
       return "No student in college." 
     return"\n".join(str(s) for s in self.students)
   

if __name__ == "__main__":
 c=College(3)

 s1=EnggStudent("E101","Ravi",21,78,"CSE",45)
 s2=MedicalStudent("M201","visha",22,75,"Cardiology",42)
 s3=Student("S301","Amit",19,55) 

 c.add_student(s1)
 c.add_student(s2)
 c.add_student(s3)

 print("----All Student in college-----")
 print(c)

 print("\n-------Get Student by ID (M201)----")
 print(c.get_student("M201"))

 print("\n-------After Removing Student E101------")
 c.remove_student("E101")
 print(c)

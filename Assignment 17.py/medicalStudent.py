from student import Student
class MedicalStudent(Student):

    def __init__(self,student_id,name,age,percentage,specialization,internship_marks):
        super().__init__(student_id,name,age,percentage)
        self.specialization = specialization
        self.internship_marks=internship_marks
    
    def accept(self):
        super().accept()
        self.specialization = input("enter Specialization:")
        self.internship_marks=float(input("Enter Internship Marks:"))

    def dispaly(self):
        super().display()
        print(f"Specialization: {self.specialization}, Internship marks:{self.internship_marks}")

    def calculate_rank(self):
        base_rank=super().calculate_rank()
        if self.internship_marks >= 40:
            return base_rank + " StrongIntern"
        return base_rank
        
    def __str__(self):
        return(f"MedicalStudent({self.student_id},{self.name},{self.age},{self.percentage},"
               f" Specialization:{self.specialization},InternshipMarks:{self.internship_marks}," 
                f"Rank: {self.calculate_rank()} )")
    
if __name__ =="__main__":
    m1=MedicalStudent("M201","visha",22,75,"Cardiology",42)
    m1.display()
    print("Rank:",m1.calculate_rank())
    print(m1)

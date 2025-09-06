from student import Student

class EnggStudent(Student):

    def __init__(self,student_id,name,age,percentage,branch,internal_marks):
        super().__init__(student_id,name,age,percentage)
        self.branch=branch
        self.internal_marks=internal_marks

    def display(self):
        super().display()
        print(f"Branch:{self.branch},Internal Marks:{self.internal_marks}")


    def accept(self):
        super().accept()
        self.branch = input("Enter Branch:")
        self.internal_marks=float(input("Enter Internal Marks:"))

    def calculate_rank(self):
        #base_rank=super().calculate_rank()
        if self.internal_marks >40:
            return "GoodInternal"
        else:
            return "Avginternal"
    
    def __str__(self):
        return(f"EnggStudent( ID:{self.student_id},Name{self.name},Age:{self.age},Percentage{self.percentage}"
                  f" Branch:{self.branch},InternalMarks:{self.internal_marks},Rank:{self.calculate_rank()})")
    

if __name__ =="__main__":
    e1=EnggStudent("E101","Ravi",21,78,"CSE",45)
    e1.display()
    print("Rank:",e1.calculate_rank())
    print(e1)
    


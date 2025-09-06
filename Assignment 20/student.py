from sy_marks import SYMarks
from ty_marks import TYMarks

class Student:
    def __init__(self,rollno,name,sy_marks:SYMarks,ty_marks:TYMarks):
        self.rollno = rollno
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def calculate_grade(self,total):
        if total >= 70 :
            return "A"
        elif total >= 60 :
            return "B"
        elif total >= 50 :
            return "c"
        elif total >= 40 :
            return "Pass Class"
        else:
            return "Fail"
        
    def display(self):
        sy_total = self.sy_marks.get_total()
        ty_total= self.ty_marks.get_total()
        total = sy_total + ty_total

        print("Roll No :",self.rollno)
        print("Name :",self.name)
        print("SY Total Marks :",sy_total)
        print("TY Total Marks :",ty_total)
        print(" Grand Total :",total)
        print("Grade :",self.calculate_grade(total))
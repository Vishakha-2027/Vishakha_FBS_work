from sy_marks import SYMarks
from ty_marks import TYMarks
from student import Student

if __name__ == "__main__":

    sy= SYMarks(60,55,50)
    ty=TYMarks(30,25)

    s= Student(101,"Ravi",sy,ty)

    s.display()
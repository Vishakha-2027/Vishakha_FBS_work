num = int(input(" Enter number of student:"))
student_count=0
total_percentage = 0

while student_count < num:
    print("Enter marks for student :" )
    subject_count = 0
    total_marks = 0

    while subject_count < 5 :
        mark = float(input(" Enter mark for subject:"))
        total_mark += mark
        subject_count+= 1
    percentage = total_mark / 5
    print(" Percentage for student")
    total_average += percentage
    student_count += 1
average_percentage = total_percentage /num
print = (" Average percentage of all students:")
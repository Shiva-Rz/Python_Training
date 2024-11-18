'''The student_grade.txt file contains the grades and student names. 
    Read the content from the file.
	Then group the grade and student name as a tuple.'''
	# Output: [("Surya", 3), ("Sathiyan", 18), ("Kiruba", 41), ("Jenish", 10), ("Sankar", 6), ("Hema", 18), ("Sundhar", 18)]

grades = []
students = []
 
file_name = input("Enter a file_name : \n")

with open(file_name, 'r') as file:
    lines = file.readlines()

    for line in range(0, len(lines)):
        if line % 2 == 0:
            grades.append(lines[line].removesuffix("\n"))
        else:
            students.append(lines[line].removesuffix("\n"))
    print(students, grades)

students_grade = list(zip(students,grades))
print(students_grade)



# students = []
# student_file = open('student_grades.txt', 'r')
# line_no = 0

# for line in student_file:
#     data = line.split()
#     print(data)    

        # students.append(line)

    # if line_no % 2 != 0:
    #     grade = student_file.readline(line_no)
    #     print(line_no)
    # else:
    #     students = student_file.readline(line_no)
    #     print(students)

# students = student_file.readlines()
# print(students)


    
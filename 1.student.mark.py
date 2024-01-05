# Initialize lists to store students, courses and marks
students = []
courses = []
marks = {}

def input_students():
    num_students = int(input("Enter number of students in a class: "))
    for _ in range(num_students):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (dd/mm/yyyy): ")
        students.append((id, name, dob))

def input_courses():
    num_courses = int(input("Enter number of courses: "))
    for _ in range(num_courses):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses.append((id, name))

def input_marks():
    course_id = input("Enter course ID for marking: ")
    for student in students:
        mark = input(f"Enter mark for student {student[1]}: ")
        marks[(student[0], course_id)] = mark

def list_courses():
    print("Courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def list_students():
    print("Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Date of Birth: {student[2]}")

def show_marks():
    course_id = input("Enter course ID to show marks: ")
    print(f"Marks for course {course_id}:")
    for student in students:
        print(f"Student {student[1]}: {marks[(student[0], course_id)]}")

# Input students and courses
input_students()
input_courses()

# Input marks for each course
for _ in range(len(courses)):
    input_marks()

# List students, courses, and marks
list_students()
list_courses()
show_marks()

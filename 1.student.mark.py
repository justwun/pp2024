# Input Functions
def input_students():
    students = []
    num_students = int(input("Enter number of students: "))
    for _ in range(num_students):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        students.append((id, name, dob))
    return students

def input_courses():
    courses = []
    num_courses = int(input("Enter number of courses: "))
    for _ in range(num_courses):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        courses.append((id, name))
    return courses

def input_marks(students, courses):
    marks = {}
    for course_id, course_name in courses:
        print(f"Entering marks for course: {course_name}")
        for student_id, student_name, _ in students:
            mark = float(input(f"Enter mark for student {student_name}: "))
            marks[(student_id, course_id)] = mark
    return marks

# Listing Functions
def list_courses(courses):
    print("Courses:")
    for id, name in courses:
        print(f"ID: {id}, Name: {name}")

def list_students(students):
    print("Students:")
    for id, name, dob in students:
        print(f"ID: {id}, Name: {name}, DoB: {dob}")

def show_student_marks(student_id, marks):
    print(f"Marks for student {student_id}:")
    for (s_id, c_id), mark in marks.items():
        if s_id == student_id:
            print(f"Course ID: {c_id}, Mark: {mark}")

# Main Function
def main():
    students = input_students()
    courses = input_courses()
    marks = input_marks(students, courses)
    
    while True:
        print("1. List courses")
        print("2. List students")
        print("3. Show student marks")
        print("4. Exit")
        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == "1":
            list_courses(courses)
        elif choice == "2":
            list_students(students)
        elif choice == "3":
            student_id = input("Enter student id to show marks: ")
            show_student_marks(student_id, marks)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

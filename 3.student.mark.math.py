import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

class MarkSheet:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self):
        num_students = int(input("Enter number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student id: ")
            name = input("Enter student name: ")
            dob = input("Enter student DoB: ")
            self.students.append(Student(student_id, name, dob))

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course id: ")
            name = input("Enter course name: ")
            credits = float(input("Enter course credits: "))
            self.courses.append(Course(course_id, name, credits))

    def input_marks(self):
        for course in self.courses:
            print(f"Entering marks for course: {course.name}")
            for student in self.students:
                mark = float(input(f"Enter mark for student {student.name}: "))
                # Use math.floor to round down to 1-digit decimal
                mark = math.floor(mark * 10) / 10
                self.marks[(student.student_id, course.course_id)] = mark

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.name}, Credits: {course.credits}")

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}")

    def show_student_marks(self, student_id):
        print(f"Marks for student {student_id}:")
        for (s_id, c_id), mark in self.marks.items():
            if s_id == student_id:
                course_name = next(course.name for course in self.courses if course.course_id == c_id)
                print(f"Course: {course_name}, Mark: {mark}")

    def calculate_gpa(self, student_id):
        marks = []
        credits = []
        for (s_id, c_id), mark in self.marks.items():
            if s_id == student_id:
                course = next(course for course in self.courses if course.course_id == c_id)
                marks.append(mark)
                credits.append(course.credits)

        if marks and credits:
            weighted_sum = np.dot(marks, credits)
            total_credits = sum(credits)
            gpa = weighted_sum / total_credits
            return round(gpa, 2)
        else:
            return None

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: self.calculate_gpa(student.student_id), reverse=True)

def main():
    mark_sheet = MarkSheet()
    mark_sheet.input_students()
    mark_sheet.input_courses()
    mark_sheet.input_marks()

    while True:
        print("1. List courses")
        print("2. List students")
        print("3. Show student marks")
        print("4. Calculate GPA for a student")
        print("5. Sort students by GPA")
        print("6. Exit")

        choice = input("Enter your choice (1, 2, 3, 4, 5, or 6): ")

        if choice == "1":
            mark_sheet.list_courses()
        elif choice == "2":
            mark_sheet.list_students()
        elif choice == "3":
            student_id = input("Enter student id to show marks: ")
            mark_sheet.show_student_marks(student_id)
        elif choice == "4":
            student_id = input("Enter student id to calculate GPA: ")
            gpa = mark_sheet.calculate_gpa(student_id)
            if gpa is not None:
                print(f"GPA for student {student_id}: {gpa}")
            else:
                print("No marks found for the student.")
        elif choice == "5":
            mark_sheet.sort_students_by_gpa()
            print("Students sorted by GPA:")
            mark_sheet.list_students()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

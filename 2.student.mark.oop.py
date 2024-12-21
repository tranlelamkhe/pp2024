def num_students():
    num_stu = int(input("Enter the number of students: "))
    return num_stu
def student_info(num_stu):
    students = []
    for i in range(num_stu):
        stu_id = input(f"Enter student ID {i+1}: ")
        stu_name = input(f"Enter student name {i+1}: ")
        dob = input(f"Enter student DOB {i+1}: ")
        students.append(Student(stu_id, stu_name, dob))
    return students
def num_courses():
    num_c = int(input("Enter the number of courses: "))
    return num_c
def course_info(num_c):
    courses = []
    for i in range(num_c):
        course_id = input(f"Enter course ID {i+1}: ")
        course_name = input(f"Enter course name {i+1}: ")
        courses.append(Course(course_id, course_name))
    return courses
def select_course(courses):
    print("Select course:")
    for i, course in enumerate(courses, 1):
        print(f"{i}. {course.course_name}")
    choice = int(input("Enter your choice: "))
    return courses[choice - 1]
def input_marks(class_inst):
    select_course = select_course(class_inst.courses)
    for student in class_inst.students:
        mark = float(input(f"Enter mark for {student.student_name} in course {select_course.course_name}: "))
        marks = Marks(student, select_course, mark)
        class_inst.add_mark(marks)
class Course:
    def __init__(self, course_id, course_name):
        self.course_name = course_name
        self.course_id = course_id
    def __str__(self):
        return f"Course ID: {self.course_id}, Course name: {self.course_name}"
class Student:
    def __init__(self,stu_id, stu_name, dob):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.dob = dob
        self.marks = {}
    def __str__(self):
        return f"Student ID: {self.stu_id}, Student name: {self.stu_name}, DoB: {self.dob}"
class Marks:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark
    def __str__(self):
        return f"Student name: {self.student.stu_name}, Course: {self.course.course_name}, Mark: {self.mark}"
class Class: 
    def __init__(self):
        self.students = []
        self.courses = []
        self.markss = []
    def add_stu(self, student):
        self.students.append(student)
    def add_course (self, course):
        self.courses.append(course)
    def add_mark(self, marks):
        self.markss.append(marks)
    def list_stu(self):
        for student in  self.students:
            print(student)
    def list_course(self):
        for course in self.courses:
            print(course)
    def show_marks(self):
        for marks in self.markss:
            print(marks)
def main():
    school = Class()
    while True:
        print("\nStudent Mark Management System")
        print("1. Input number of students")
        print("2. Input number of courses")
        print("3. Input student info")
        print("4. Input course info")
        print("5. Input marks for a course")
        print("6. List all courses")
        print("7. List all students")
        print("8. Show student marks for a given course")
        print("9. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            num_students_value = num_students()
        elif choice == "2":
            num_courses_value = num_courses()
        elif choice == "3":
            if num_students_value == 0:
                print("Input the number of students first")
            else:
                students = student_info(num_students_value)
                for student in students:
                    school.add_stu(student)
        elif choice == "4":
            if num_courses_value == 0:
                print("Input the number of courses first")
            else:
                courses = course_info(num_courses_value)
                for course in courses:
                    school.add_course(course)
        elif choice == "5":
            if not school.students or not school.courses:
                print("Input student and course info first")
            else:
                input_marks(school)
        elif choice == "6":
            school.list_course()
        elif choice == "7":
            school.list_stu()
        elif choice == "8":
            if not school.students or not school.courses:
                print("Input student and course info first")
            else:
                school.show_marks()
        elif choice == "9":
            print("Exiting")
            break
        else:
            print("Try again")
if __name__ == "__main__":
    main()    
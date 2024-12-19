# input func
def num_students():
    num_stu = int(input("Enter the number of students: "))
    return num_stu
def student_info(num_stu):
    students = []
    for i in range(num_stu):
        stu_id = input(f"Enter student ID {i+1}: ")
        stu_name = input(f"Enter student name {i+1}: ")
        dob = input(f"Enter student DOB {i+1}: ")
        students.append({"Student ID": stu_id, "Student name": stu_name, "DoB": dob, "Marks": {}})
    return students
def num_courses():
    num_c = int(input("Enter the number of courses: "))
    return num_c
def course_info(num_c):
    courses = []
    for i in range(num_c):
        course_id = input(f"Enter course ID {i+1}: ")
        course_name = input(f"Enter course name {i+1}: ")
        courses.append((course_id, course_name))
    return courses
def select_course(courses):
    print("Select course:")
    for i, course in enumerate(courses, 1):
        print(f"{i}. {course[1]}")
    choice = int(input("Enter your choice: "))
    return courses[choice - 1][0]
def input_marks(students, courses):
    course_id = select_course(courses)
    for student in students:
        mark = float(input(f"Enter mark for {student["Student name"]} in course {course_id}: "))
        student["Marks"][course_id] = mark
# list func
def list_stu(students):
    for student in students:
        print(f"Student ID: {student["Student ID"]}, Name: {student["Student name"]}, DOB: {student["DoB"]}")
def list_courses(courses):
    for course in courses:
        print(f"Course ID: {course[0]}, Course name: {course[1]}")
def show_marks(students, courses):
    course_id = select_course(courses)
    print(f"\nMark of student in course {course_id}:")
    for student in students:
        mark = student["Marks"].get(course_id, "No input")
        print(f"Student {student["Student name"]} (ID: {student["Student ID"]}) - Marks: {mark}")
def main():
    students = []
    courses = []
    num_students_value = 0
    num_courses_value = 0
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
        elif choice == "4":
            if num_courses_value == 0:
                print("Input the number of courses first")
            else:
                courses = course_info(num_courses_value)
        elif choice == "5":
            if not students or not courses:
                print("Input student and course info first")
            else:
                input_marks(students, courses)
        elif choice == "6":
            list_courses(courses)
        elif choice == "7":
            list_stu(students)
        elif choice == "8":
            if not students or not courses:
                print("Input student and course info first.")
            else:
                show_marks(students, courses)
        elif choice == "9":
            print("Exiting")
            break
        else:
            print("Try again")
if __name__ == "__main__":
    main()    
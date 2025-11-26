# Student Record Management System
# Using: Dictionary, Lists, tuple, set
students = {}
student_ids = set()
courses = ("CSE", "CSD", "ML", "AI", "ECE", "EEE")

def add_student():
    student_id = input("Enter Student ID: ")
    if student_id in student_ids:
        print("Student ID already exists. Please try again.")
        return
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    print("Available Courses: ", ", ".join(courses))
    course = input("Enter Course: ")
    if course not in courses:
        print("Invalid course. Please try again.")
        return
    students[student_id] = {"Name": name, "Age": age, "Course": course}
    student_ids.add(student_id)
    print("Student added successfully.")

def view_students():
    if not students:
        print("No students found.")
        return
    print("\n--- Student Records ---")
    for student_id, info in students.items():
        print(f"ID: {student_id}, Name: {info['Name']}, Age: {info['Age']}, Course: {info['Course']}")      

def search_student():
    student_id = input("Enter Student ID to search: ")
    if student_id in students:
        info = students[student_id]
        print(f"ID: {student_id}, Name: {info['Name']}, Age: {info['Age']}, Course: {info['Course']}")
    else:
        print("Student not found.") 
    
def delete_student():
    student_id = input("Enter Student ID to delete: ")
    if student_id in students:
        del students[student_id]
        student_ids.remove(student_id)
        print("Student deleted successfully.")
    else:
        print("Student not found.")


while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4.Delete Student")
    print("5. Exit")


    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()    
    elif choice == "5":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")



    

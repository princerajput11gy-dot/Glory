students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")
    
    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }
    
    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No records found.\n")
        return
    
    print("\nStudent Records:")
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")
    print()


def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s["roll"] == roll:
            print(f"Found: Name: {s['name']}, Marks: {s['marks']}\n")
            return
    print("Student not found.\n")


def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!\n")
            return
    print("Student not found.\n")


while True:
    print("===== Student Record System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
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
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again.\n")

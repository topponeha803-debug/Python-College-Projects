students = {}

def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Name: ")
    course = input("Enter Course: ")
    age = input("Enter Age: ")

    students[roll] = {
        "name": name,
        "course": course,
        "age": age
    }

    print("Student added!")


def search_student():
    roll = input("Enter Roll Number: ")

    if roll not in students:
        print("Student not found!")
        return

    s = students[roll]

    print("\n--- Student Details ---")
    print("Roll:", roll)
    print("Name:", s["name"])
    print("Course:", s["course"])
    print("Age:", s["age"])


def delete_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        del students[roll]
        print("Student deleted!")
    else:
        print("Student not found!")


def show_students():
    if not students:
        print("No records found!")
        return

    for roll, s in students.items():
        print(
            roll,
            "|",
            s["name"],
            "|",
            s["course"],
            "|",
            s["age"]
        )


while True:
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Show Students")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        show_students()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")

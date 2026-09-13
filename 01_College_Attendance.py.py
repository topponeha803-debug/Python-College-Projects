students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    if roll in students:
        print("Student already exists!")
        return

    students[roll] = {
        "name": name,
        "present": 0,
        "absent": 0
    }

    print("Student added successfully!")


def mark_attendance():
    roll = input("Enter Roll Number: ")

    if roll not in students:
        print("Student not found!")
        return

    status = input("Enter P for Present or A for Absent: ").upper()

    if status == "P":
        students[roll]["present"] += 1
        print("Marked Present")
    elif status == "A":
        students[roll]["absent"] += 1
        print("Marked Absent")
    else:
        print("Invalid choice!")


def show_attendance():
    roll = input("Enter Roll Number: ")

    if roll not in students:
        print("Student not found!")
        return

    s = students[roll]
    total = s["present"] + s["absent"]

    if total == 0:
        percentage = 0
    else:
        percentage = s["present"] / total * 100

    print("\n--- Attendance Details ---")
    print("Roll:", roll)
    print("Name:", s["name"])
    print("Present:", s["present"])
    print("Absent:", s["absent"])
    print("Percentage:", round(percentage, 2), "%")


def show_all():
    for roll, s in students.items():
        total = s["present"] + s["absent"]

        if total:
            percentage = s["present"] / total * 100
        else:
            percentage = 0

        print(
            roll,
            s["name"],
            round(percentage, 2), "%"
        )


while True:
    print("\n===== ATTENDANCE SYSTEM =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Show All Students")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        show_attendance()
    elif choice == "4":
        show_all()
    elif choice == "5":
        print("Program closed.")
        break
    else:
        print("Invalid choice!")

tasks = []

def add_task():
    task = input("Enter new task: ")

    tasks.append({
        "task": task,
        "completed": False
    })

    print("Task added!")


def show_tasks():
    if not tasks:
        print("No tasks available!")
        return

    print("\n===== YOUR TASKS =====")

    for number, item in enumerate(tasks, start=1):

        if item["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(
            number,
            ".",
            item["task"],
            "-",
            status
        )


def complete_task():
    show_tasks()

    if not tasks:
        return

    number = int(input("Enter task number: "))

    if 1 <= number <= len(tasks):
        tasks[number - 1]["completed"] = True
        print("Task completed!")
    else:
        print("Invalid task number!")


def delete_task():
    show_tasks()

    if not tasks:
        return

    number = int(input("Enter task number: "))

    if 1 <= number <= len(tasks):
        deleted = tasks.pop(number - 1)
        print("Deleted:", deleted["task"])
    else:
        print("Invalid task number!")


while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")

patients = {}

def add_patient():
    patient_id = input("Enter Patient ID: ")

    if patient_id in patients:
        print("Patient already exists!")
        return

    name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    disease = input("Enter Disease: ")
    doctor = input("Enter Doctor Name: ")

    patients[patient_id] = {
        "name": name,
        "age": age,
        "disease": disease,
        "doctor": doctor
    }

    print("Patient added successfully!")


def search_patient():
    patient_id = input("Enter Patient ID: ")

    if patient_id not in patients:
        print("Patient not found!")
        return

    p = patients[patient_id]

    print("\n--- Patient Details ---")
    print("ID:", patient_id)
    print("Name:", p["name"])
    print("Age:", p["age"])
    print("Disease:", p["disease"])
    print("Doctor:", p["doctor"])


def show_patients():
    if not patients:
        print("No patient records!")
        return

    for pid, p in patients.items():
        print(
            pid,
            "|",
            p["name"],
            "|",
            p["disease"],
            "| Doctor:",
            p["doctor"]
        )


while True:
    print("\n===== HOSPITAL MANAGEMENT =====")
    print("1. Add Patient")
    print("2. Search Patient")
    print("3. Show All Patients")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        search_patient()
    elif choice == "3":
        show_patients()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")

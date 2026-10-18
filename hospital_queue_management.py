"""Hospital Queue Management System
Python Programming Lab - Project Based Learning (PBL)

Educational console-based project. This is not a clinical triage tool.
Patient information is kept in memory and is cleared when the program exits.
"""

from collections import deque


class Patient:
    """Store the details of one patient."""

    def __init__(self, patient_id, name, age, problem, priority=0):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.problem = problem
        self.priority = priority

    def display(self):
        priority_names = {0: "Normal", 1: "High", 2: "Medium", 3: "Low"}
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Medical problem: {self.problem}")
        print(f"Type/Priority: {priority_names[self.priority]}")


normal_queue = deque()
emergency_queue = []
next_patient_id = 1001


def read_patient_details(priority):
    """Read and validate patient details, then return a Patient object."""
    global next_patient_id

    while True:
        name = input("Enter patient name: ").strip()
        if name:
            break
        print("Name cannot be empty. Please try again.")

    while True:
        try:
            age = int(input("Enter patient age: "))
            if age > 0:
                break
            print("Age must be a positive number.")
        except ValueError:
            print("Please enter age as a whole number.")

    while True:
        problem = input("Enter medical problem: ").strip()
        if problem:
            break
        print("Medical problem cannot be empty. Please try again.")

    patient = Patient(next_patient_id, name, age, problem, priority)
    next_patient_id += 1
    return patient


def add_normal_patient():
    patient = read_patient_details(0)
    normal_queue.append(patient)
    print("\nNormal patient registered successfully.")
    patient.display()


def add_emergency_patient():
    print("\nEmergency priority options:")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    while True:
        try:
            priority = int(input("Choose priority (1-3): "))
            if priority in (1, 2, 3):
                break
            print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a number.")

    patient = read_patient_details(priority)
    emergency_queue.append(patient)
    # A smaller number means a higher priority. Python's sort is stable.
    emergency_queue.sort(key=lambda item: item.priority)
    print("\nEmergency patient registered successfully.")
    patient.display()


def serve_next_patient():
    if emergency_queue:
        patient = emergency_queue.pop(0)
        print("\nServing emergency patient:")
    elif normal_queue:
        patient = normal_queue.popleft()
        print("\nServing normal patient:")
    else:
        print("\nNo patients are waiting.")
        return
    patient.display()


def show_normal_queue():
    if not normal_queue:
        print("\nNormal queue is empty.")
        return

    print("\n--- NORMAL PATIENT QUEUE (arrival order) ---")
    for patient in normal_queue:
        patient.display()
        print("-" * 35)


def show_emergency_queue():
    if not emergency_queue:
        print("\nEmergency queue is empty.")
        return

    print("\n--- EMERGENCY PATIENT QUEUE (priority order) ---")
    for patient in emergency_queue:
        patient.display()
        print("-" * 35)


def search_waiting_patient():
    print("\nSearch options:")
    print("1. Search by Patient ID")
    print("2. Search by Patient Name")
    choice = input("Choose search option (1-2): ").strip()
    waiting_patients = list(normal_queue) + list(emergency_queue)

    if choice == "1":
        try:
            target_id = int(input("Enter patient ID: "))
        except ValueError:
            print("Patient ID must be a number.")
            return
        matches = [p for p in waiting_patients if p.patient_id == target_id]
    elif choice == "2":
        target_name = input("Enter patient name: ").strip().casefold()
        if not target_name:
            print("Name cannot be empty.")
            return
        matches = [p for p in waiting_patients if p.name.casefold() == target_name]
    else:
        print("Invalid search option. Please choose 1 or 2.")
        return

    if matches:
        print("\nMatching waiting patient(s):")
        for patient in matches:
            patient.display()
            print("-" * 35)
    else:
        print("No matching waiting patient found.")


def main():
    while True:
        print("\n========== HOSPITAL QUEUE MANAGEMENT SYSTEM ==========")
        print("1. Add normal patient")
        print("2. Add emergency patient")
        print("3. Serve next patient")
        print("4. View normal queue")
        print("5. View emergency queue")
        print("6. Search waiting patient")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()
        if choice == "1":
            add_normal_patient()
        elif choice == "2":
            add_emergency_patient()
        elif choice == "3":
            serve_next_patient()
        elif choice == "4":
            show_normal_queue()
        elif choice == "5":
            show_emergency_queue()
        elif choice == "6":
            search_waiting_patient()
        elif choice == "7":
            print("Thank you for using Hospital Queue Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()

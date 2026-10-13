import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not load student records. Starting with an empty list.")

    return []


def save_students():
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
    except OSError:
        print("Error: Could not save student records!")


students = load_students()

while True:
    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
    print("1. Add a student")
    print("2. View all students")
    print("3. Search for a student")
    print("4. Delete a student")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        name = input("Enter student name: ").strip()

        try:
            marks = float(input("Enter student marks (0-100): "))

            if not name:
                print("Student name cannot be empty!")
            elif marks < 0 or marks > 100:
                print("Marks must be between 0 and 100!")
            else:
                students.append({"name": name, "marks": marks})
                save_students()
                print("Student added and saved successfully!")

        except ValueError:
            print("Please enter valid numeric marks!")

    elif choice == "2":
        if students:
            print("\n===== ALL STUDENTS =====")

            for number, student in enumerate(students, start=1):
                print(
                    f"{number}. {student['name']} - "
                    f"{student['marks']}/100"
                )
        else:
            print("No student records found.")

    elif choice == "3":
        search_name = input(
            "Enter the student name to search: "
        ).strip()

        found = False

        for student in students:
            if student["name"].lower() == search_name.lower():
                print("\nStudent found!")
                print("Name:", student["name"])
                print("Marks:", student["marks"], "/100")
                found = True

        if not found:
            print("Student not found.")

    elif choice == "4":
        delete_name = input(
            "Enter the student name to delete: "
        ).strip()

        found = False

        for student in students:
            if student["name"].lower() == delete_name.lower():
                students.remove(student)
                save_students()
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "5":
        print("Goodbye, bro! 👋")
        break

    else:
        print("Invalid option! Please choose 1-5.")
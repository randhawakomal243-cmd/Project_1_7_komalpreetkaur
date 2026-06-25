"""
Program: Student Grade Tracker
Author: Komalpreet Kaur
Purpose: Simple system to manage student grades
Date: June 25, 2026
"""

students = {}

def menu():
    print("\n--- Student Grade Tracker ---")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. View Students")
    print("4. Calculate Average")
    print("5. Exit")

while True:
    menu()
    choice = input("Choose option: ")

    if choice == "1":
    name = input("Enter student name: ")

    if name not in students:
        students[name] = []
        print("Student added successfully.")
    else:
        print("Student already exists.")

    if choice == "2":
        name = input("Student name: ")

        if name in students:
            grade = float(input("Enter grade: "))
            students[name].append(grade)
            print("Grade added.")
        else:
            print("Student not found.")

    elif choice == "3":
        print(students)

    elif choice == "4":
        name = input("Student name: ")

        if name in students and len(students[name]) > 0:
            avg = sum(students[name]) / len(students[name])
            print("Average:", round(avg, 2))
        else:
            print("No grades found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
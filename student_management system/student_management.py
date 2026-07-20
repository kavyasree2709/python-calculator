import os

FILE_NAME = "students.txt"

def load_students():
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                roll, name, marks = line.strip().split(",")
                students.append({
                    "roll": roll,
                    "name": name,
                    "marks": float(marks)
                })
    return students


def save_students(students):
    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(f"{student['roll']},{student['name']},{student['marks']}\n")


def add_student(students):
    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:
            print("Student with this roll number already exists.")
            return

    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    students.append({
        "roll": roll,
        "name": name,
        "marks": marks
    })

    save_students(students)
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n------ Student Records ------")
    print("{:<10} {:<20} {:<10}".format("Roll", "Name", "Marks"))

    for student in students:
        print("{:<10} {:<20} {:<10}".format(
            student["roll"],
            student["name"],
            student["marks"]
        ))


def search_student(students):
    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found")
            print("Roll :", student["roll"])
            print("Name :", student["name"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


def delete_student(students):
    roll = input("Enter Roll Number to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            delete_student(students)

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
students = {}

# Add students
students[input("Enter first student name: ")] = input("Enter grade: ")
students[input("Enter second student name: ")] = input("Enter grade: ")
students[input("Enter third student name: ")] = input("Enter grade: ")

# Update a student's grade
update_name = input("Enter the name of the student to update: ")

if update_name in students:
    students[update_name] = input("Enter the new grade: ")
    print("Grade updated successfully.")
else:
    print("Student not found.")

# Print all student grades
print("\nStudent Grades:")

for student, grade in students.items():
    print(f"{student}: {grade}")
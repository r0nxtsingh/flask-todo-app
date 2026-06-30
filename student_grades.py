from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []
students = {}

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    data = request.get_json()

    item_name = data.get('itemName')
    item_description = data.get('itemDescription')

    todos.append({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return jsonify({
        "message": "Todo item stored successfully"
    })

# Existing student grades functionality
students[input("Enter first student name: ")] = input("Enter grade: ")
students[input("Enter second student name: ")] = input("Enter grade: ")
students[input("Enter third student name: ")] = input("Enter grade: ")

update_name = input("Enter the name of the student to update: ")

if update_name in students:
    students[update_name] = input("Enter the new grade: ")
    print("Grade updated successfully.")
else:
    print("Student not found.")

print("\nStudent Grades:")

for student, grade in students.items():
    print(f"{student}: {grade}")

if __name__ == '__main__':
    app.run(debug=True)

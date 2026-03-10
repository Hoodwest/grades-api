from flask import Flask, jsonify, request
# Flask = the web framework, jsonify = converts Python to JSON, request = reads incoming data

# Create the app
app = Flask(__name__)

# This is our "database" — just a list in memory, resets every time you restart the server
grades = [
    {"student_id": "S001", "name": "Alice", "grade": 88},
    {"student_id": "S002", "name": "Bob", "grade": 74},
]

# ENDPOINT 1: GET /grades
# When someone visits /grades, return the full list
@app.route("/grades", methods=["GET"])
def get_all_grades():
    return jsonify(grades), 200  # 200 = OK

# ENDPOINT 2: POST /grades
# When someone sends new student data, validate it then save it
@app.route("/grades", methods=["POST"])
def add_grade():
    data = request.get_json()  # Read the JSON they sent

    # Check 1: Did they send anything at all?
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400  # 400 = Bad Request

    # Check 2: Did they include all 3 required fields?
    required_fields = ["student_id", "name", "grade"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Check 3: Is the grade actually a number (not something like "A+")?
    if not isinstance(data["grade"], (int, float)):
        return jsonify({"error": "Grade must be a number"}), 400

    # Check 4: Is the grade between 0 and 100?
    if not (0 <= data["grade"] <= 100):
        return jsonify({"error": "Grade must be between 0 and 100"}), 400

    # Check 5: Does this student ID already exist in our list?
    for g in grades:
        if g["student_id"] == data["student_id"]:
            return jsonify({"error": "Student ID already exists"}), 409  # 409 = Conflict

    # All checks passed — add the new student to the list
    grades.append(data)
    return jsonify({"message": "Grade added successfully"}), 201  # 201 = Created

# ENDPOINT 3: GET /grades/<student_id>
# When someone visits e.g. /grades/S001, find and return that specific student
@app.route("/grades/<student_id>", methods=["GET"])
def get_grade(student_id):
    for g in grades:
        if g["student_id"] == student_id:
            return jsonify(g), 200  # Found — return their record

    # If the loop finishes without finding a match, return 404
    return jsonify({"error": "Student not found"}), 404  # 404 = Not Found

# Start the server (debug=True shows errors clearly, never use in a real live app)
if __name__ == "__main__":
    app.run(debug=True)
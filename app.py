from flask import Flask, jsonify, request
from flasgger import Swagger

 # Create the Flask app
app = Flask(__name__)
swagger  = Swagger(app)

# This list acts as our database — it lives in memory while the server runs
grades = [
{"student_id": "S001", "name": "Alice", "grade": 88},
{"student_id": "S002", "name": "Bob", "grade": 74},

]
# ENDPOINT 1: GET /grades

@app.route("/grades", methods=["GET"])
def get_all_grades():
    return jsonify(grades), 200

# ENDPOINT 2: POST /grades 
@app.route("/grades", methods=["POST"])
def add_grade():
    data = request.get_json()

    # Validation check 1: Is there any JSON body at all? 
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400


    # Validation check 2: Are all required fields present? 

    required_fields = ["student_id", "name", "grade"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    #  Validation check 3: Is grade a number?
    if not isinstance(data["grade"], (int, float)):
        return jsonify({"error": "Grade must be a number"}), 400


    # Validation check 4: Is grade between 0 and 100? 

    if not (0 <= data["grade"] <= 100):
        return jsonify({"error": "Grade must be between 0 and 100"}), 400

    # Validation check 5: Does this student ID already exist? 

    for g in grades:
        if g["student_id"] == data["student_id"]:
                return jsonify({"error": "Student ID already exists"}), 409


    # All checks passed — save the new grade

    grades.append(data)
    return jsonify({"message": "Grade added successfully"}), 201

#ENDPOINT 3: GET /grades/
@app.route("/grades/<student_id>", methods=["GET"])
def get_grade(student_id):
    for g in grades:
        if g["student_id"] == student_id:
            return jsonify(g), 200

# If we get here, no match was found
    return jsonify({"error": "Student not found"}), 404

# START THE SERVER 
if __name__ == "__main__":
 app.run(debug=True)

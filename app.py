from flask import Flask, request, jsonify
from Gestion import Student, Course, Enrollment
from data import students, courses

app = Flask(__name__)

@app.route('/students', methods=['POST'])
def create_student():

    data = request.get_json()
    student = Student(data['name'], data['studentID'], data['age'])
    students[data['studentID']] = student
    return jsonify({"message": "Etudiant créé avec succès "}), 201

@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    course = Course(data['courseName'], data['courseCode'], data['creditHours'])
    courses[data['courseCode']] = course
    return jsonify({"message": "Cour créé avec succès "}), 201

@app.route('/enrollments', methods=['POST'])
def enroll_student():
    data = request.get_json()
    student = students.get(data['studentID'])
    course = courses.get(data['courseCode'])
    if student and course:
        course.enrollStudent(student)
        return jsonify({"message": "Étudiant inscrit avec succès"}), 201
    return jsonify({"error": "Etudiant ou cour introuvable"}), 404

@app.route('/students/<studentID>', methods=['GET'])
def get_student(studentID):
    student = students.get(studentID)
    if student:
        return jsonify({
            "name": student.name,
            "age": student.age,
            "average_grade": student.getAverageGrade()
        })
    return jsonify({"error": "Étudiant introuvable"}), 404

@app.route('/courses/<courseCode>', methods=['GET'])
def get_course(courseCode):
    course = courses.get(courseCode)
    if course:
        return jsonify({
            "courseName": course.courseName,
            "enrolled_students": course.getEnrolledStudents()
        })
    return jsonify({"error": "Cours introuvable"}), 404
@app.route('/')
def home():
    return "Bienvenue sur mon API Flask 🚀"

if __name__ == '__main__':
    app.run(debug=True)

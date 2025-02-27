class Student:
    """Représente un étudiant"""
    def __init__(self, name, studentID, age):
        self.name = name
        self.studentID = studentID
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        """Ajoute une note à l'étudiant"""
        self.grades.append(grade)

    def get_average_grade(self):
        """Retourne la moyenne des notes de l'étudiant"""
        return sum(self.grades) / len(self.grades) if self.grades else 0
    
class Course:
    """Représente un cours"""
    def __init__(self, course_name, course_code, credit_hours):
        self.course_name = course_name
        self.course_code = course_code
        self.credit_hours = credit_hours
        self.students = []

    def enroll_student(self, student):
        """Ajoute un étudiant au cours"""
        self.students.append(student)

    def get_enrolled_students(self):
        """Retourne la liste des étudiants inscrits"""
        return [s.name for s in self.students]
     
class Enrollment:
    """Représente une inscription d'un étudiant à un cours"""
    def __init__(self, student, course):
        self.student = student
        self.course = course

    def register(self):
        """Inscrit l'étudiant au cours"""
        self.course.enroll_student(self.student)

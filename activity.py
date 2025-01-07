class Student:
    def __init__(self, student_id, name, dob, grade_level, gpa, courses, contact):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.grade_level = grade_level
        self.gpa = gpa
        self.courses = courses
        self.contact = contact

class StudentRecords:
    def __init__(self):
        self.students = {}

    def add(self, student):
        self.students[student.student_id] = student

    def get(self, student_id):
        return self.students.get(student_id)

    def update(self, student_id, **kwargs):
        student = self.get(student_id)
        if student:
            for key, value in kwargs.items():
                setattr(student, key, value)

    def list(self):
        return self.students.values()

    def delete(self, student_id):
        self.students.pop(student_id, None)


# Example usage
records = StudentRecords()
records.add(Student(1, "John Doe", "2005-03-15", 10, 3.8, ["Math", "Science"], "john.doe@example.com"))

# Print student name
print(records.get(1).name)  # Output: John Doe

# Update GPA and list students
records.update(1, gpa=3.9)
for student in records.list():
    print(student.name, student.gpa)

# Delete student
records.delete(1)
class Student:
    def __init__(self, student_id, name, age, courses, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = courses
        self.grade = grade

class StudentRecords:
    def __init__(self):
        self.records = {}

    def add_student(self, student):
        self.records[student.student_id] = student

    def remove_student(self, student_id):
        self.records.pop(student_id, None)

    def get_student(self, student_id):
        return self.records.get(student_id)

    def update_student(self, student_id, **kwargs):
        student = self.records.get(student_id)
        if student:
            for key, value in kwargs.items():
                setattr(student, key, value)

# Example usage
records = StudentRecords()
student1 = Student(1, 'John Doe', 20, ['Math', 'Physics'], 'A')
student2 = Student(2, 'Jane Smith', 22, ['Biology', 'Chemistry'], 'B')

records.add_student(student1)
records.add_student(student2)

print(records.get_student(1).name)  # Output: John Doe
print(records.get_student(2).courses)  # Output: ['Biology', 'Chemistry']

records.update_student(1, grade='A+')
print(records.get_student(1).grade)  # Output: A+

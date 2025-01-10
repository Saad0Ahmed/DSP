class Student:
    def __init__(self, student_id, name, age, major, gpa):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}, GPA: {self.gpa}"

class StudentRecords:
    def __init__(self):
        self.records = []

    def add_student(self, student):
        self.records.append(student)

    def remove_student(self, student_id):
        self.records = [student for student in self.records if student.student_id != student_id]

    def get_student(self, student_id):
        for student in self.records:
            if student.student_id == student_id:
                return student
        raise ValueError("Student ID not found.")

    def __str__(self):
        return "\n".join(str(student) for student in self.records)

#example usage
if __name__ == "__main__":
    records = StudentRecords()

    # Adding students
    records.add_student(Student(1, "Alice", 20, "Computer Science", 3.5))
    records.add_student(Student(2, "Bob", 21, "Mathematics", 3.8))
    records.add_student(Student(3, "Charlie", 22, "Physics", 3.2))

    # Display all students
    print("All Students:")
    print(records)

    # Get a specific student
    print("\nGet Student with ID 2:")
    print(records.get_student(2))

    # Remove a student
    print("\nRemoving Student with ID 1.")
    records.remove_student(1)

    # Display all students after removal
    print("\nAll Students after removal:")
    print(records)

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    def display_info(self):
        print(f"Имя: {my_student.name}, ID: {my_student.student_id}")
        
my_student = Student("Руслан", "123")
my_student.display_info()

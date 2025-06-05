class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    def display_info(self):
        print(f"Имя: {my_student.name}, ID: {my_student.student_id}")
        
my_student = Student("Галя", "123")
my_student.display_info()
        
class Group:
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def show_students(self):
        if not self.students:
            print("Группа пуста.")
        else:
            for student in self.students:
                student.display_info()
group = Group()
print(group.students)
group.add_student(my_student)  
for student in group.students:
    my_student.display_info()

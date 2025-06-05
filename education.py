class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    def display_info(self):
        print(f"Имя: {my_student.name}, ID: {my_student.student_id}")
    def add_grade(self, grade): 
        self.grades.append(grade)
    def get_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades) 
    
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
student.add_grade(5)
student.add_grade(4)
print(f"Средняя оценка: {student.get_average():.2f}")

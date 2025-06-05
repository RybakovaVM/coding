class Student:
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id
        self.__grades = []
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__student_id
    def get_grades(self):
        return self.__grades
    def display_info(self):
        print(f"Имя: {my_student.__name}, ID: {my_student.__student_id}")
    def add_grade(self, grade): 
        self.__grades.append(grade)
    def get_average(self):
        if not self.__grades:
            return 0.0
        return sum(self.__grades) / len(self.__grades) 
    
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

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
        print(f"Имя: {self.__name}, ID: {self.__student_id}")
    def add_grade(self, grade): 
        self.__grades.append(grade)
    def get_average(self):
        if not self.__grades:
            return 0.0
        return sum(self.__grades) / len(self.__grades) 
    
my_student1 = Student("Галя", "123")
my_student2 = Student("Оля", "555")
my_student1.display_info()
my_student2.display_info()
        
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
    def find_by_name(self, name):
        finded = False
        for student in self.students:
            if name == student.get_name():
                print(f'Студент по имени {name} найден')
                student.display_info()
                finded = True       
        if not finded:
            print(f"Студент не найден")
group = Group()
print(group.students)
group.add_student(my_student1)
for student in group.students:
    my_student1.display_info()
my_student1.add_grade(5)
my_student2.add_grade(4)
print(f"Средняя оценка: {my_student1.get_average():.2f}")
print(f"Средняя оценка: {my_student2.get_average():.2f}")

import sqlite3
import random

conn = sqlite3.connect('university.db')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS students ")
cur.execute("DROP TABLE IF EXISTS courses")

cur.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT NOT NULL,
    age  TEXT NOT NULL,
    cours TEXT NOT NULL
)
""")

cur.execute("""
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS student_courses (
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (course_id) REFERENCES courses (id),
    PRIMARY KEY (student_id, course_id)
)
""")

courses = [
    "Математика",
    "Физика", 
    "Программирование",
    "История",
    "Английский язык"
]

names = [
    "Irina", "Olga", "Anna", "Boris", "Clara", "Dima", "Masha",
    "David", "Elena", "Fedor", "Galina", "Igor", "Sveta", 
    "Ivan", "Katya", "Vova", "Maks", "Nikita", "Pavel", "Sergei"
]

students_data = []
for i in range(20):
    name = f"{random.choice(names)}"
    age = random.randint(18,25)  
    cours = random.choice(courses)  
    
    students_data.append((name, age, cours))

cur.executemany("INSERT INTO students (name, age, cours) VALUES (?, ?, ?)", students_data)

for course in courses:
    cur.execute("INSERT INTO courses (name) VALUES (?)", (course,))

cur.execute("SELECT id FROM courses")
course_ids = [row[0] for row in cur.fetchall()]

cur.execute("SELECT id FROM students")
student_ids = [row[0] for row in cur.fetchall()]

student_courses_data = []
for student_id in student_ids:
    num_courses = random.randint(1, 4)
    selected_courses = random.sample(course_ids, num_courses)
    
    for course_id in selected_courses:
        student_courses_data.append((student_id, course_id))

cur.executemany("INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)", student_courses_data)

conn.commit()

print("\nКоличество студентов на каждом курсе:")
cur.execute("""
SELECT c.name, COUNT(sc.student_id) as student_count
FROM courses c
LEFT JOIN student_courses sc ON c.id = sc.course_id
GROUP BY c.id
ORDER BY student_count DESC
""")

course_stats = cur.fetchall()
for course_name, student_count in course_stats:
    print(f"  {course_name}: {student_count} студентов")

print("\nСредний возраст студентов:")
for row in cur.execute("SELECT AVG(age) FROM students"):
    print(round(row[0], 1))

print("\nОБЩАЯ СТАТИСТИКА:")
cur.execute("SELECT COUNT(*) FROM students")
total_students = cur.fetchone()[0]
print(f"Всего студентов: {total_students}")

cur.execute("SELECT COUNT(*) FROM courses")
total_courses = cur.fetchone()[0]
print(f"Всего курсов: {total_courses}")

cur.execute("SELECT COUNT(*) FROM student_courses")
total_enrollments = cur.fetchone()[0]
print(f"Всего записей о зачислении: {total_enrollments}")

conn.close()

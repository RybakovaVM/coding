CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age int NOT NULL,
    group_id VARCHAR(100) NOT NULL
);

CREATE TABLE `groups` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    group_name VARCHAR(100) NOT NULL
);

CREATE TABLE courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    teacher_id int NOT NULL
);

CREATE TABLE teachers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE enrollments (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    course_id VARCHAR(100) NOT NULL,
    grade int NOT NULL
);

INSERT INTO students (name, age, group_id)
VALUES 
('Анна Иванова', 18, 123),
('Петр Смирнов', 19, 124),
('Сергей Кузнецов', 20, 125),
('Мария Сабитова', 20, 125),
('Варвара Клюшкина', 20, 123);

SELECT * FROM students;

INSERT INTO `groups` (group_name)
VALUES 
('ИТ-101'),
('ИТ-102'), 
('Мат-201'),
('Физ-301'),
('Хим-401');

SELECT * FROM `groups`;

INSERT INTO courses (course_name, teacher_id)
VALUES 
('Программирование на Python', 1),
('Базы данных', 5),
('Высшая математика', 2),
('Квантовая физика', 3),
('Органическая химия', 4);

SELECT * FROM courses;

INSERT INTO teachers (name)
VALUES 
('Артем Петров'),
('Ваня Лукашик'),
('Анастасия Рашитова'),
('Радик Рустамович'),
('Павел Иванович');

SELECT * FROM teachers;

INSERT INTO enrollments (student_id, course_id, grade)
VALUES 
(1, 1, 5),
(2, 2, 4),
(3, 1, 4),
(4, 3, 5),
(5, 2, 3);

SELECT * FROM enrollments;

SELECT s.name AS student_name, g.group_name
FROM students s
JOIN `groups` g ON s.group_id = g.id
ORDER BY s.name;

SELECT name AS student_name, age, g.group_name
FROM students s
JOIN `groups` g ON s.group_id = g.id
WHERE age > 20
ORDER BY age DESC, name;

SELECT c.course_name AS course, t.name AS teacher
FROM courses c
JOIN teachers t ON c.teacher_id = t.id
ORDER BY t.name, c.course_name;

SELECT s.name AS student_name, c.course_name AS course, e.grade AS grade, g.group_name
FROM students s
JOIN enrollments e ON s.id = e.student_id
JOIN courses c ON e.course_id = c.id
JOIN `groups` g ON s.group_id = g.id
WHERE e.grade > 85
ORDER BY e.grade DESC, s.name;

SELECT s.name AS student_name, g.group_name
FROM students s
JOIN `groups` g ON s.group_id = g.id
ORDER BY s.name;

SELECT g.group_name, COUNT(s.id) AS number_of_students, ROUND(AVG(s.age), 1) AS average_age
FROM `groups` g
LEFT JOIN students s ON g.id = s.group_id
GROUP BY g.id, g.group_name
ORDER BY g.group_name;

SELECT c.course_name, t.name AS teacher
FROM courses c
LEFT JOIN enrollments e ON c.id = e.course_id
JOIN teachers t ON c.teacher_id = t.id
WHERE e.course_id IS NULL
ORDER BY c.course_name;

SELECT s.id, s.name AS student_name, s.age, g.group_name
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id
JOIN `groups` g ON s.group_id = g.id
WHERE e.student_id IS NULL
ORDER BY s.name;

SELECT s.id, s.name AS student_name, g.group_name, COUNT(e.grade) AS number_of_grades, ROUND(AVG(e.grade), 2) AS average_grade
FROM students s
JOIN enrollments e ON s.id = e.student_id
JOIN `groups` g ON s.group_id = g.id
GROUP BY s.id, s.name, g.group_name
HAVING COUNT(e.grade) >= 1
ORDER BY average_grade DESC
LIMIT 3;

SELECT c.course_name, t.name AS teacher, COUNT(e.student_id) AS number_of_students
FROM courses c
LEFT JOIN enrollments e ON c.id = e.course_id
JOIN teachers t ON c.teacher_id = t.id
GROUP BY c.id, c.course_name, t.name
ORDER BY number_of_students DESC, c.course_name;

SELECT t.id, t.name AS teacher_name, COUNT(c.id) AS number_of_courses, GROUP_CONCAT(c.course_name ORDER BY c.course_name SEPARATOR ', ') AS courses_list
FROM teachers t
JOIN courses c ON t.id = c.teacher_id
GROUP BY t.id, t.name
HAVING COUNT(c.id) > 1
ORDER BY number_of_courses DESC, t.name;

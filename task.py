import sqlite3
import datetime

def create_database():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        name TEXT,
        age INTEGER,
        weight REAL,
        height REAL,
        bmi REAL,
        result TEXT
    )
    ''')
    
    conn.commit()

def save_person(name, age, weight, height, bmi, result):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    cursor.execute('''
    INSERT INTO people (date, name, age, weight, height, bmi, result)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (current_time, name, age, weight, height, bmi, result))
    
    conn.commit()

def show_history():
    cursor.execute('SELECT * FROM people ORDER BY date DESC')
    people = cursor.fetchall()
    
    
    if not people:
        print("Пока нет записей в базе данных")
        return
    
    print("\n История исследований:")
    for person in people:
        print(f"{person[1]} | {person[2]} лет | {person[3]}кг | {person[4]}см")
        print(f"ИМТ: {person[5]} - {person[6]}")
        print("-" * 50)

def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m * height_m)
    return round(bmi, 1)

def get_bmi_result(bmi, age):
    if age < 18:
        if bmi < 16:
            return "Сильный недовес (детский)"
        elif bmi < 18.5:
            return "Небольшой недовес (детский)"
        elif bmi < 25:
            return "Нормальный вес (детский)"
        elif bmi < 30:
            return "Избыток веса (детский)"
        else:
            return "Ожирение (детский)"
    
    elif 18 <= age < 25:
        if bmi < 18:
            return "Недостаток веса (молодежь)"
        elif bmi < 24:
            return "Нормальный вес (молодежь)"
        elif bmi < 29:
            return "Избыток веса (молодежь)"
        else:
            return "Ожирение (молодежь)"
    
    elif 25 <= age < 45:
        if bmi < 19:
            return "Недостаток веса (взрослые)"
        elif bmi < 26:
            return "Нормальный вес (взрослые)"
        elif bmi < 30:
            return "Избыток веса (взрослые)"
        else:
            return "Ожирение (взрослые)"
    
    elif 45 <= age < 60:
        if bmi < 20:
            return "Недостаток веса (средний возраст)"
        elif bmi < 27:
            return "Нормальный вес (средний возраст)"
        elif bmi < 32:
            return "Избыток веса (средний возраст)"
        else:
            return "Ожирение (средний возраст)"
    
    else:
        if bmi < 22:
            return "Недостаток веса (пожилые)"
        elif bmi < 28:
            return "Нормальный вес (пожилые)"
        elif bmi < 33:
            return "Избыток веса (пожилые)"
        else:
            return "Ожирение (пожилые)"

def get_normal_weight_range(height, age):
    height_m = height / 100
    
    if age < 18:
        min_normal = 18.5 * (height_m * height_m)
        max_normal = 24.9 * (height_m * height_m)
    elif 18 <= age < 25:
        min_normal = 18.0 * (height_m * height_m)
        max_normal = 23.9 * (height_m * height_m)
    elif 25 <= age < 45:
        min_normal = 19.0 * (height_m * height_m)
        max_normal = 25.9 * (height_m * height_m)
    elif 45 <= age < 60:
        min_normal = 20.0 * (height_m * height_m)
        max_normal = 26.9 * (height_m * height_m)
    else:
        min_normal = 22.0 * (height_m * height_m)
        max_normal = 27.9 * (height_m * height_m)
    
    return round(min_normal, 1), round(max_normal, 1)

def get_age_group(age):
    if age < 18:
        return "дети и подростки"
    elif 18 <= age < 25:
        return "молодежь (18-24)"
    elif 25 <= age < 45:
        return "взрослые (25-44)"
    elif 45 <= age < 60:
        return "средний возраст (45-59)"
    else:
        return "пожилые (60+)"
    
def main():
    create_database()
    
    print(" Калькулятор ИМТ с учетом возраста")
    
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    weight = float(input("Введите вес (кг): "))
    height = float(input("Введите рост (см): "))
    
    bmi = calculate_bmi(weight, height)
    result = get_bmi_result(bmi, age)
    age_group = get_age_group(age)
    min_normal, max_normal = get_normal_weight_range(height, age)
    
    save_person(name, age, weight, height, bmi, result)
    
    print("\n Результат:")
    print(f"Возрастная группа: {age_group}")
    print(f"ИМТ: {bmi}")
    print(f"Результат: {result}")
    print(f"Нормальный вес для вашего роста и возраста: {min_normal} - {max_normal} кг")
    
    if "Недостаток" in result or "недовес" in result:
        print(" Совет: рекомендуется увеличить питание")
    elif "Избыток" in result or "Ожирение" in result:
        print(" Совет: рекомендуется больше двигаться")
    else:
        print(" Отлично! Так держать!")

conn = sqlite3.connect('bmi_database.db')
cursor = conn.cursor()

def show_menu():
    while True:
        print("Главное меню:")
        print("1. Сделать новое исследование")
        print("2. Показать историю")
        print("3. Показать возрастные нормы")
        print("4. Выйти")
        
        choice = input("Выберите вариант (1-4): ")
        
        if choice == "1":
            main()
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("\n Возрастные нормы ИМТ:")
            print(" Дети и подростки: 18.5 - 24.9")
            print(" Молодежь (18-24): 18.0 - 23.9")
            print(" Взрослые (25-44): 19.0 - 25.9")
            print(" Средний возраст (45-59): 20.0 - 26.9")
            print(" Пожилые (60+): 22.0 - 27.9")
        elif choice == "4":
            print("До свидания! ")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

print("Добро пожаловать в программу исследования ИМТ!")
show_menu()

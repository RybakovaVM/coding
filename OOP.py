class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2 

def print_area(shape):
    print(f"Площадь фигуры: {shape.area():.2f}")

rect = Rectangle(4, 5)
circle = Circle(3)
print_area(rect)   
print_area(circle) 

class Animal:
    def make_sound(self):
        print("Животное издаёт звук")

class Dog(Animal):
    def make_sound(self):
        print("Гав-гав!")

class Cat(Animal):
    def make_sound(self):
        print("Мяу-мяу!")

animals = [Dog(), Cat(), Dog(), Animal(), Cat()]

for animal in animals:
    animal.make_sound()
    
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  
        self.__balance = balance                
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Счёт пополнен на {amount}. Новый баланс: {self.__balance}")
        else:
            print("Ошибка: сумма для пополнения должна быть положительной.")
    
    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Со счёта снято {amount}. Новый баланс: {self.__balance}")
            else:
                print("Ошибка: недостаточно средств на счёте.")
        else:
            print("Ошибка: сумма для снятия должна быть положительной.")
    
    def get_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number

account = BankAccount("123456789", 1000000000000)

try:
    print(account.__balance)
except AttributeError as e:
    print(f"Ошибка доступа к приватному полю: {e}")

print("Номер счёта:", account.get_account_number())
print("Текущий баланс:", account.get_balance())

account.deposit(500)    
account.withdraw(200)  
account.withdraw(2000) 
account.deposit(-100)
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self):
        return f'Книга: "{self.title}", автор: {self.author}, год издания: {self.year}.'
   
book1 = Book("Война и мир", "Лев Толстой", 1869)
book2 = Book("1984", "Джордж Оруэлл", 1949)
book3 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)

print(book1.get_info())
print(book2.get_info())
print(book3.get_info())

import json
import os

class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def get_info(self):
        print(f'{self.name}, {self.author}, {self.year}')

    def to_dict(self):
        return {
            "name": self.name,
            "author": self.author,
            "year": self.year
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["author"], data["year"])


class Library:
    def __init__(self, filename="library.json"):
        self.books = []
        self.filename = filename
        self.load()

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.name}' добавлена в библиотеку")
        self.save()

    def remove_book(self, book_name):
        for book in self.books:
            if book.name == book_name:
                self.books.remove(book)
                print(f"Книга '{book_name}' удалена из библиотеки")
                self.save()
                return
        print(f"Книга '{book_name}' не найдена")

    def show_all_books(self):
        if not self.books:
            print("В библиотеке нет книг")
            return
        print("Список книг в библиотеке:")
        for book in self.books:
            book.get_info()

    def save(self):
        try:
            data = [book.to_dict() for book in self.books]
            with open(self.filename, "w", encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"Данные успешно сохранены в файл {self.filename}")
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")

    def load(self):
        try:
            if not os.path.exists(self.filename):
                print(f"Файл {self.filename} не найден. Будет создан новый.")
                return
            
            with open(self.filename, "r", encoding='utf-8') as f:
                data = json.load(f)
                self.books = [Book.from_dict(item) for item in data]
            print(f"Данные успешно загружены из файла {self.filename}")
            
        except json.JSONDecodeError:
            print(f"Ошибка: файл {self.filename} поврежден. Будет создан новый.")
        except Exception as e:
            print(f"Неизвестная ошибка при загрузке данных: {e}")


# Основная программа
if __name__ == "__main__":
    my_library = Library()
    
    while True:
        print("\nДоступные действия:")
        print("1 - Добавить книгу")
        print("2 - Удалить книгу")
        print("3 - Показать все книги")
        print("4 - Выйти")
        
        choice = input("Выберите действие (1-4): ")
        
        if choice == '1':
            name = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            new_book = Book(name, author, year)
            my_library.add_book(new_book)
        elif choice == '2':
            book_name = input("Введите название книги для удаления: ")
            my_library.remove_book(book_name)
        elif choice == '3':
            my_library.show_all_books()
        elif choice == '4':
            print("Выход из программы")
            break
        else:
            print("Неверный ввод, пожалуйста, выберите 1-4")

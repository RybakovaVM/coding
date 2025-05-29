from abc import ABC, abstractmethod

class LibraryUser(ABC):
    name = ''
    user_id = 0
    
    @abstractmethod
    def borrow_book(book)
        pass
    
    @abstractmethod
    def return_book(book)
        pass

class Student(LiberaryUser):
    limit = 3
    borrowed_books = []
    
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        
        def borrow_book(book):
            # первая проверка
            if len(borrowed_books) == limit:
                print("ты не можешь взять больше книг")
                return
            
            # проверяем, не взята ли эта книга студентом
            if book in borrowed_books:
                print("Эта книга уже у тебя")
                return
            # проверяем, не взята ли эта книга кем-то
            if not book.available:
                print("книга кем-то взята")
            # если проверки пройдены выдать книгу
            borrowed_books.append(book)
            print("молодец, читай")
            book.available = False
            
        def return_book(book):
            self.borrowed_books.remove(book)
            book.available = False
    
class Teacher(LiberaryUser):
    limit = 5
    borrowed_books = []
    
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        
    # первая проверка
            if len(borrowed_books) == limit:
                print("ты не можешь взять больше книг")
                return
            
            # проверяем, не взята ли эта книга студентом
            if book in borrowed_books:
                print("Эта книга уже у тебя")
                return
            # проверяем, не взята ли эта книга кем-то
            if not book.available:
                print("книга кем-то взята")
            # если проверки пройдены выдать книгу
            borrowed_books.append(book)
            print("молодец, читай")
            book.available = False
            
class Book:
    title, author, isdn, available
    
    def __init__(self, title, author, isdn)
    self.title = title
    self.author = author
    self.isdn = isdn
    self.available = True
    
class Liberary:
    books = []
    
    def add_book(book):
        books.append(book)
        
    def remove_book(book):
        books.remove(book)
        
    def find_book_by_title(title):
        for book in books:
        if book.title == title:
            print('Книга найдена')
            return
    print('Такой книги нет')

def list_available_books():
    for book in books:
        if book.available:
            print(book.title)

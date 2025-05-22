from abc import ABC, abstractmethod
class LibraryUser(ABC):
    def __init__(self, name, user_id)
        self.name = name
        self.user_id = user_id
    @abstractmethod
    def borrow_book(book):
        
        
    @abstractmethod
    def return_book(book):
    

class Student(LibraryUser):
    def __init__(self, name, user_id)
    super().__init__(name, user_id)
    self.borrowed_books = []
    self.max_books = 3
    
    borrow_book = []
        
    def borrow_book(title):
        book = self.library.remove_book(title)
        if book:
            borrowed_books.append(book)
        
    
    def return_book(self, book):
        self.library.add_boo.
        

class Teacher(LibraryUser):
    borrowed_books = []

class Book:
    def __init__(self, title, author, isbn, available)
    self.title = title
    self.author = author
    self.isbn = isbn
    self.available = available


class Library:
    books = []
    
    
# создаем и заполняем библиотеку книгами
books = []
book = Book("", "")
books.append(book)    

book = Book("", "")
books.append(book)   

book = Book("", "")
books.append(book)   

library = Library(books)

# создаем студента и учителя
student = Student
teacher = Teacher
    
    
    
    
    
    
    

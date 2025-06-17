class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def get_info(self):
        print(f'{self.name}, {self.author}, {self.year}')

class Library:
  def __init__(self):
    self.books = []

  def add_book(self, book):
    self.books.append(book)
    print(f"Книга '{book.name}' добавлена в библиотеку")

  def remove_book(self, book_name):
    for book in self.books:
      if book.name == book_name:
        self.books.remove(book)
        print(f"Книга '{book_name}' удалена из библиотеки")
        return
      print(f"Книга '{book_name}' не найдена")

  def show_all_books(self):
    if not self.books:
      print("В библиотеке нет книг")
      return
    print("Список книг в библиотеке")
    for book in self.books:
      book.get_info()
my_library = Library()
book1 = Book("Война и мир", "Лев Толстой", 1869)
book2 = Book("Преступление и наказание", "Фёдор Достоевский", 1866)
my_library.add_book(book1)
my_library.add_book(book2)
my_library.show_all_books()
my_library.remove_book("Война и мир")
my_library.show_all_books()

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Library:
    def __init__(self):
        self.books = []  # Lista para armazenar objetos do tipo Book

    def add_book(self, book):
        """Adiciona um livro à coleção."""
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, title):
        """Remove um livro da coleção pelo título."""
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def list_books(self):
        """Lista todos os livros na coleção."""
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")

# Exemplo de uso
library = Library()

# Criando objetos do tipo Book
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

# Adicionando livros à biblioteca
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Listando os livros
library.list_books()

# Removendo um livro
library.remove_book("1984")

# Listando os livros novamente
library.list_books()

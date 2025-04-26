# 11. Class Methods
# Create a class Book with a class variable total_books. 
# Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0 # Class variable to keep track of total books

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()  # Increment count when a new book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"📚 Total books: {cls.total_books}")


# Create book instances
book1 = Book("Python Programming")
book2 = Book("OOP Concepts")
book4 = Book("Machine Learning")


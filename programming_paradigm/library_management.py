# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private-like attribute

    def check_out(self):
        """Marks the book as checked out if available."""
        if self._is_checked_out:
            print(f"'{self.title}' is already checked out.")
        else:
            self._is_checked_out = True

    def return_book(self):
        """Marks the book as available again."""
        if not self._is_checked_out:
            print(f"'{self.title}' was not checked out.")
        else:
            self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private-like list to store Book objects

    def add_book(self, book):
        """Adds a Book object to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"You checked out '{title}'.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """Returns a book by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                print(f"You returned '{title}'.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """Lists all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books currently available.")


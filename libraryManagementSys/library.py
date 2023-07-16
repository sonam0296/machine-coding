class Book:
    def __init__(self, book_id, title, authors, publishers):
        self.book_id = book_id
        self.title = title
        self.authors = authors
        self.publishers = publishers


class BookCopy:
    def __init__(self, copy_id, book, rack_number):
        self.copy_id = copy_id
        self.book = book
        self.rack_number = rack_number
        self.borrowed_by = None
        self.due_date = None


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.book_copies = []
        self.racks = {}
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_book_copy(self, book_copy):
        self.book_copies.append(book_copy)
        self.racks[book_copy.rack_number] = book_copy

    def remove_book_copy(self, copy_id):
        for book_copy in self.book_copies:
            if book_copy.copy_id == copy_id:
                if book_copy.borrowed_by:
                    print("Cannot remove a borrowed book copy.")
                else:
                    del self.racks[book_copy.rack_number]
                    self.book_copies.remove(book_copy)
                    print("Book copy removed successfully.")
                return
        print("Book copy not found.")

    def borrow_book(self, book_id, user_id, due_date):
        if len(self.users) <= user_id:
            print("User not found.")
            return

        if len(self.users[user_id].borrowed_books) >= 5:
            print("User has reached the maximum limit of borrowed books.")
            return

        for book_copy in self.book_copies:
            if book_copy.book.book_id == book_id and not book_copy.borrowed_by:
                book_copy.borrowed_by = user_id
                book_copy.due_date = due_date
                self.users[user_id].borrowed_books.append(book_copy.copy_id)
                print("Book borrowed successfully.")
                return
        print("Book copy not available.")

    def return_book(self, copy_id):
        for book_copy in self.book_copies:
            if book_copy.copy_id == copy_id and book_copy.borrowed_by is not None:
                user_id = book_copy.borrowed_by
                book_copy.borrowed_by = None
                book_copy.due_date = None
                self.racks[book_copy.rack_number] = book_copy
                self.users[user_id].borrowed_books.remove(copy_id)
                print("Book returned successfully.")
                return
        print("Book copy not found or not borrowed.")

    def print_borrowed_books(self, user_id):
        if len(self.users) <= user_id or len(self.users[user_id].borrowed_books) == 0:
            print("You haven't borrowed any books.")
            return
        print("Borrowed Book Copy IDs:")
        for copy_id in self.users[user_id].borrowed_books:
            print(copy_id)

    def search_books(self, query):
        results = []
        query = query.lower()
        for book_copy in self.book_copies:
            book = book_copy.book
            if (
                query in str(book.book_id).lower()
                or query in book.title.lower()
                or query in book.authors.lower()
                or query in book.publishers.lower()
            ):
                results.append(book_copy)
        return results

def main():
    library = Library()

    # Creating books
    book1 = Book(1, "Mahabharata", "Author 1", "Publisher 1")
    book2 = Book(2, "Ramayan", "Author 2", "Publisher 2")

    # Adding books to the library
    library.add_book(book1)
    library.add_book(book2)

    # Creating book copies
    book_copy1 = BookCopy(101, book1, 1)
    book_copy2 = BookCopy(102, book1, 2)
    book_copy3 = BookCopy(201, book2, 1)

    # Adding book copies to the library racks
    library.add_book_copy(book_copy1)
    library.add_book_copy(book_copy2)
    library.add_book_copy(book_copy3)

    # Creating users
    user1 = User(1, "John")
    user2 = User(2, "Alice")

    # Adding users to the library
    library.users.append(user1)
    library.users.append(user2)

    # Test functionalities
    library.borrow_book(1, 1, "2023-07-31")
    library.borrow_book(1, 2, "2023-07-30")
    library.borrow_book(2, 2, "2023-07-29")
    library.print_borrowed_books(2)
    library.return_book(101)

    query = input("Enter your search query (Book ID, Title, Author, or Publisher): ")
    search_results = library.search_books(query)
    if not search_results:
            print("No books found matching the search query.")
    else:
        print("Search Results:")
        for book_copy in search_results:
            book = book_copy.book
            print("Copy ID:", book_copy.copy_id)
            print("Book ID:", book.book_id)
            print("Title:", book.title)
            print("Authors:", book.authors)
            print("Publishers:", book.publishers)
            print("Rack Number:", book_copy.rack_number)
            if book_copy.borrowed_by is not None:
                print("Status: Borrowed by User ID", book_copy.borrowed_by)
                print("Due Date:", book_copy.due_date)
            else:
                print("Status: Available")
            print("---------------------------")


if __name__ == "__main__":
    main()

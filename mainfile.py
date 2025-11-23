# An assignment on how to handle books in libraries to tell if they are issued, reserved,available, and also add new books   in the system. This asignment uses classes and objects to represent books and their statuses, this uses the concepts of OOP.
# I am dividing the project into segments:
# 1. Create a Book class with attributes like title, author, ISBN, and status (available, issued, reserved).
# 2. inventory design, with sub parts which inlcude codes for adding books, issuing books, reserving books, and checking book status.
# 3. creating a catalog to save and load data using simple CSV/text file
# 4. creating a menu driven command for easy navigation.

# import logging

# configure basic logging for the module
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# Step 1: Define the Book class
# from asyncio.log import logger


class Book:
    def __init__(self, title, author, isbn, status='available'):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    # def is_available(self):
    #     """Return True if the book is available for issuing."""
    #     return self.status == 'available'

    def issue_book(self):
        if self.status == 'available':
            self.status = 'issued'
            # logger.info('Issued book: %s (ISBN: %s)', self.title, self.isbn)
            print(f'Book "{self.title}" has been issued.')
        else:
            # logger.info('Attempted to issue unavailable book: %s (status=%s)', self.title, self.status)
            print(f'Book "{self.title}" is not available for issuing.')

    def reserve_book(self):
        if self.status == 'available':
            self.status = 'reserved'
            # logger.info('Reserved book: %s (ISBN: %s)', self.title, self.isbn)
            print(f'Book "{self.title}" has been reserved.')
        else:
            # logger.info('Attempted to reserve unavailable book: %s (status=%s)', self.title, self.status)
            print(f'Book "{self.title}" is not available for reserving.')

    def return_book(self):
        if self.status in ['issued', 'reserved']:
            self.status = 'available'
            # logger.info('Returned book: %s (ISBN: %s)', self.title, self.isbn)
            print(f'Book "{self.title}" has been returned and is now available.')
        else:
            # logger.info('Attempted to return a book that was not issued/reserved: %s (status=%s)', self.title, self.status)
            print(f'Book "{self.title}" was not issued or reserved.')

    def check_status(self):
        # logger.debug('Checked status for book: %s (status=%s)', self.title, self.status)
        print(f'Book "{self.title}" is currently {self.status}.')
# Step 2: Define the Library class to manage the collection of books/and designing inventory 
class Library:
    def __init__(self):
        self.catalog = {}

    def add_book(self, book):
        self.catalog[book.title] = book
        # logger.info('Added book to catalog: %s (ISBN: %s)', book.title, book.isbn)
        print(f'Book "{book.title}" added to the library catalog.')

    def issue_book(self, title):
        if title in self.catalog:
            self.catalog[title].issue_book()
        else:
            # logger.warning('Issue attempt for missing book title: %s', title)
            print('Book not found in the catalog.')

    def reserve_book(self, title):
        if title in self.catalog:
            self.catalog[title].reserve_book()
        else:
            # logger.warning('Reserve attempt for missing book title: %s', title)
            print('Book not found in the catalog.')

    def return_book(self, title):
        if title in self.catalog:
            self.catalog[title].return_book()
        else:
            # logger.warning('Return attempt for missing book title: %s', title)
            print('Book not found in the catalog.')

    def check_book_status(self, title):
        if title in self.catalog:
            self.catalog[title].check_status()
        else:
            # logger.warning('Status check for missing book title: %s', title)
            print('Book not found in the catalog.')

    def display_catalog(self):
        if not self.catalog:
            print('The catalog is empty.')
        else:
            print('\n--- Library Catalog ---')
            for title, book in self.catalog.items():
                print(f'Title: {title}, Author: {book.author}, ISBN: {book.isbn}, Status: {book.status}')
            print('--- End of Catalog ---\n')

    def update_book(self, current_title, new_title=None, author=None, isbn=None):
        if current_title in self.catalog:
            book = self.catalog[current_title]
            if new_title and new_title != current_title:
                book.title = new_title
                self.catalog[new_title] = book
                del self.catalog[current_title]
                current_title = new_title
            if author:
                book.author = author
            if isbn:            
                book.isbn = isbn
            # logger.info('Updated book: %s (ISBN: %s)', book.title, book.isbn)
            print(f'Book "{book.title}" has been updated successfully.')
        else:
            print('Book not found in the catalog.')
            # logger.warning('Attempted update for missing book title: %s', current_title)
# step 3 creating a catalog to save and load data using simple CSV/text file
    def save_catalog(self, filename):
        with open(filename, 'w') as file:
            for book in self.catalog.values():
                file.write(f'{book.title}|{book.author}|{book.isbn}|{book.status}\n')
        # logger.info('Catalog saved to %s (entries=%d)', filename, len(self.catalog))
        print('Catalog saved successfully.')

    def load_catalog(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split('|')
                    if len(parts) != 4:
                        print(f'Warning: skipping malformed catalog line: {line}')
                        continue
                    title, author, isbn, status = parts
                    try:
                        book = Book(title, author, isbn, status)
                        self.add_book(book)
                    except Exception as e:
                        print(f'Warning: failed to load book from line: {line} ({e})')
            # logger.info('Catalog loaded from %s', filename)
            print('Catalog loaded successfully.')
        except FileNotFoundError:
            # logger.warning('Catalog file not found: %s', filename)
            print('Catalog file not found.')

    def search_by_title(self, title_query):
        """Search catalog by title. Case-insensitive substring match. Returns list of matching books."""
        if not title_query:
            print('No title provided for search.')
            return []
        matches = []
        q = title_query.strip().lower()
        for book in self.catalog.values():
            if q in book.title.lower():
                matches.append(book)
        # logger.info('Searched by title: "%s" -> %d matches', title_query, len(matches))
        if matches:
            for b in matches:
                print(f'Title: {b.title}, Author: {b.author}, ISBN: {b.isbn}, Status: {b.status}')
        else:
            print('No books matched that title.')
        return matches

    def search_by_isbn(self, isbn_query):
        """Search catalog by ISBN. Exact or substring match. Returns list of matching books."""
        if not isbn_query:
            print('No ISBN provided for search.')
            return []
        matches = []
        q = isbn_query.strip().lower()
        for book in self.catalog.values():
            if q in book.isbn.lower():
                matches.append(book)
        # logger.info('Searched by ISBN: "%s" -> %d matches', isbn_query, len(matches))
        if matches:
            for b in matches:
                print(f'Title: {b.title}, Author: {b.author}, ISBN: {b.isbn}, Status: {b.status}')
        else:
            print('No books matched that ISBN.')
        return matches

    def is_available(self, title):
        # """Return True/False if a given book title is available. Prints a message too."""
        if title in self.catalog:
            avail = self.catalog[title].is_available()
            # logger.info('Availability check for %s: %s', title, avail)
            print(f'Book "{title}" availability: {avail}')
            return avail
        else:
            # logger.warning('Availability check for missing book title: %s', title)
            print('Book not found in the catalog.')
            return False
# step 4 creating a menu driven command for easy navigation.
def main():
    library = Library()
    library.load_catalog('library_catalog.txt')

    while True:
        print('\nLibrary Menu:')
        print('1. Add Book')
        print('2. Issue Book')
        print('3. Reserve Book')
        print('4. Return Book')
        print('5. Check Book Status')
        print('6. Display Entire Catalog')
        print('7. Update Book')
        print('8. Save Catalog')
        print('9. Exit')
        print('10. Search by Title')
        print('11. Search by ISBN')
        print('12. Check Availability')

        choice = input('Enter your choice (1-12): ')

        if choice == '1':
            title = input('Enter book title: ')
            author = input('Enter book author: ')
            isbn = input('Enter book ISBN: ')
            book = Book(title, author, isbn)
            library.add_book(book)
        elif choice == '2':
            title = input('Enter book title to issue: ')
            library.issue_book(title)
        elif choice == '3':
            title = input('Enter book title to reserve: ')
            library.reserve_book(title)
        elif choice == '4':
            title = input('Enter book title to return: ')
            library.return_book(title)
        elif choice == '5':
            title = input('Enter book title to check status: ')
            library.check_book_status(title)
        elif choice == '6':
            library.display_catalog()
        elif choice == '7':
            current_title = input('Enter book title to update: ')
            updated_title = input ('Update book title (press Enter to skip):')
            author = input('Update book author (press Enter to skip): ')
            isbn = input('Update book ISBN (press Enter to skip): ')
            library.update_book(current_title, updated_title if updated_title else None, author if author else None, isbn if isbn else None)
        elif choice == '8':
            library.save_catalog('library_catalog.txt')
        elif choice == '10':
            title_q = input('Enter title or part of title to search: ')
            library.search_by_title(title_q)
        elif choice == '11':
            isbn_q = input('Enter ISBN or part of ISBN to search: ')
            library.search_by_isbn(isbn_q)
        elif choice == '12':
            title = input('Enter book title to check availability: ')
            library.is_available(title)
        elif choice == '9':
            print('Exiting the library system.')
            break
        else:
            print('Invalid choice. Please try again.')





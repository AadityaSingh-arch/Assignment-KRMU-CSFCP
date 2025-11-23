from library_manager.book import Book
from library_manager.inventory import Library
from library_manager.cli import main
# from library_manager.data.library_catalog import library_catalog
def main():
    library = Library()
    library.load_catalog('library_catalog.txt') 
    
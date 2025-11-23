import json
import logging
from pathlib import Path
from library_manager.book import Book

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class LibraryInventory:
    def _init_(self, filepath="data/catalog.json"):
        self.filepath = Path(filepath)
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            if self.filepath.exists():
                with open(self.filepath, "r") as f:
                    data = json.load(f)
                    self.books = [Book(**item) for item in data]
            else:
                self.save_books()
        except Exception as e:
            logging.error("Error loading file: %s", e)
            self.books = []

    def save_books(self):
        try:
            self.filepath.parent.mkdir(exist_ok=True)
            with open(self.filepath, "w") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=4)
        except Exception as e:
            logging.error("Error saving file: %s", e)

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        self.save_books()
        logging.info("Added book: %s", title)

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    def display_all(self):
        return self.books
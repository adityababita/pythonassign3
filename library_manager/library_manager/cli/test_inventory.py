import unittest
from library_manager.inventory import LibraryInventory

class TestInventory(unittest.TestCase):
    def test_add_book(self):
        inv = LibraryInventory(filepath="data/test_catalog.json")
        inv.add_book("Test Book", "Author", "12345")
        self.assertEqual(inv.books[-1].title, "Test Book")

if __name__ == '_main_':
    unittest.main()
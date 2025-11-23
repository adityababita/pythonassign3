from library_manager.inventory import LibraryInventory

def menu():
    print("\n--- Library Inventory Manager ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")
    return input("Choose an option: ")

def main():
    inv = LibraryInventory()

    while True:
        choice = menu()

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            inv.add_book(title, author, isbn)
            print("Book added successfully!")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = inv.search_by_isbn(isbn)
            if book and book.issue():
                inv.save_books()
                print("Book issued!")
            else:
                print("Book unavailable or not found.")

        elif choice == "3":
            isbn = input("ISBN to return: ")
            book = inv.search_by_isbn(isbn)
            if book:
                book.return_book()
                inv.save_books()
                print("Book returned.")
            else:
                print("Book not found.")

        elif choice == "4":
            books = inv.display_all()
            for b in books:
                print(b)

        elif choice == "5":
            title = input("Enter title: ")
            results = inv.search_by_title(title)
            for b in results:
                print(b)
            if not results:
                print("No match found.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "_main_":
    main()
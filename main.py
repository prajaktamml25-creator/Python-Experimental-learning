books = []

def add_book():
    book_id = input("Book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    books.append({"id": book_id, "title": title, "author": author})
    print("Book added successfully!")

def view_books():
    for book in books:
        print(book)

def main():
    while True:
        print("\n1. Add Book")
        print("2. View Books")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

main()

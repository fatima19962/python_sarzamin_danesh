
from user import User
from manager import Manager
from book import Book

# -------------------------
# Global Data
# -------------------------
users = {}            # username -> User
books = {}            # book_id  -> Book
manager = Manager()
total_sales = 0


# -------------------------
# Helper Functions
# -------------------------
def view_books():
    print("\n--- Book List ---")
    if not books:
        print("No books available.")
        return

    for b in books.values():
        print(b)


def add_book():
    print("\n--- Add Book ---")
    book_id = input("Book ID: ")

    if book_id in books:
        print("Book ID already exists!")
        return

    name = input("Book Name: ")
    price = float(input("Book Price: "))
    stock = int(input("Stock: "))

    books[book_id] = Book(book_id, name, price, stock)
    print("Book added successfully!")


def show_book_count():
    total_titles = len(books)
    total_stock = sum(b.stock for b in books.values())

    print("\n--- Book Count ---")
    print(f"Total titles: {total_titles}")
    print(f"Total stock: {total_stock}")


def user_buy_book(user):
    global total_sales
    view_books()
    book_id = input("Enter Book ID to buy: ")

    if book_id not in books:
        print("Invalid book ID!")
        return

    book = books[book_id]

    if user.buy_book(book):
        total_sales += book.price
        print("Purchase successful!")
    else:
        print("Book out of stock!")


def show_user_history(user):
    print("\n--- Purchase History ---")
    if not user.history:
        print("No purchases yet.")
        return

    for item in user.history:
        print("-", item)


# -------------------------
# User Menu
# -------------------------
def user_menu(user):
    while True:
        print("\n--- User Menu ---")
        print("1. View Books")
        print("2. Buy Book")
        print("3. View Purchase History")
        print("4. Logout")
        choice = input("Choose: ")

        if choice == "1":
            view_books()
        elif choice == "2":
            user_buy_book(user)
        elif choice == "3":
            show_user_history(user)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")


# -------------------------
# Manager Menu
# -------------------------
def manager_menu():
    while True:
        print("\n--- Manager Menu ---")
        print("1. Add Book")
        print("2. View Book Count")
        print("3. View Total Sales")
        print("4. Logout")
        choice = input("Choose: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            show_book_count()
        elif choice == "3":
            print(f"Total Sales: {total_sales}")
        elif choice == "4":
            break
        else:
            print("Invalid choice!")


# -------------------------
# Authentication
# -------------------------
def register_user():
    print("\n--- Register User ---")
    username = input("Username: ")

    if username in users:
        print("User already exists!")
        return

    password = input("Password: ")
    users[username] = User(username, password)
    print("Registration successful!")


def login_user():
    print("\n--- User Login ---")
    username = input("Username: ")
    password = input("Password: ")

    user = users.get(username)
    if user and user.password == password:
        print("Login successful!")
        user_menu(user)
    else:
        print("Invalid login!")


def login_manager():
    print("\n--- Manager Login ---")
    username = input("Username: ")
    password = input("Password: ")

    if username == manager.username and password == manager.password:
        print("Manager login successful!")
        manager_menu()
    else:
        print("Invalid manager credentials!")


# -------------------------
# Main Menu
# -------------------------
def main():
    while True:
        print("\n=== Library Shop System ===")
        print("1. Register")
        print("2. User Login")
        print("3. Manager Login")
        print("4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            login_manager()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


main()

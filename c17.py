# Creating and testing a robust library system implementation.
from datetime import datetime, date
from pprint import pprint

def create_library_system():
    """Return a dict of functions that operate on an internal library state."""
    # ---------- Data ----------
    BOOKS = {
        1: {'title': 'c#',      'author': 'erfan', 'borrowers': [], 'count': 5},
        2: {'title': 'java',    'author': 'erfan', 'borrowers': [], 'count': 5},
        3: {'title': 'python',  'author': 'erfan', 'borrowers': [], 'count': 5},
        4: {'title': 'flutter', 'author': 'erfan', 'borrowers': [], 'count': 5},
    }

    MEMBERS = {
        101: {'name': 'sara',    'email': 'test@gmail.com', 'borrow_books': []},
        102: {'name': 'fatemeh', 'email': 'test@gmail.com', 'borrow_books': []},
        103: {'name': 'maryam',  'email': 'test@gmail.com', 'borrow_books': []},
        104: {'name': 'zahra',   'email': 'test@gmail.com', 'borrow_books': []}
    }

    history = []

    # ---------- Helpers ----------
    def _parse_date(s):
        """Parse 'YYYY-MM-DD' string -> date object. Return None if invalid."""
        if isinstance(s, date):
            return s
        try:
            return datetime.strptime(s, "%Y-%m-%d").date()
        except Exception:
            print("Invalid date. Use YYYY-MM-DD.")
            return None

    def _is_available(book):
        return book['count'] > 0

    # ---------- Display ----------
    def display_books():
        print('\n---------------- Book List ---------------')
        for book_id, book in BOOKS.items():
            status = 'available' if _is_available(book) else 'not available'
            print(f"{book_id}) {book['title']} - {book['author']} - {status} ({book['count']} copies)")

    def display_members():
        print('\n---------------- Member List ---------------')
        for member_id, member in MEMBERS.items():
            print(f"{member_id}) {member['name']} - {member['email']} - Borrowed: {len(member['borrow_books'])}")

    # ---------- Add ----------
    def add_book(title_book, author_book, count):
        new_id = max(BOOKS.keys()) + 1 if BOOKS else 1
        BOOKS[new_id] = {
            'title': str(title_book),
            'author': str(author_book),
            'borrowers': [],
            'count': int(count)
        }
        history.append(f"[ADD-BOOK] '{title_book}' by {author_book} ({count} copies)")
        return new_id

    def add_member(name, email):
        new_id = max(MEMBERS.keys()) + 1 if MEMBERS else 101
        MEMBERS[new_id] = {'name': str(name), 'email': str(email), 'borrow_books': []}
        history.append(f"[ADD-MEMBER] '{name}' <{email}>")
        return new_id

    # ---------- Borrow / Return ----------
    def borrow_book(book_id, member_id, date_borrow, date_return):
        # existence checks
        if book_id not in BOOKS:
            print('Cannot find this book')
            return False
        if member_id not in MEMBERS:
            print('Cannot find this member')
            return False

        book = BOOKS[book_id]
        member = MEMBERS[member_id]

        # availability and limits
        if book['count'] <= 0:
            print('Book is not available')
            return False
        if len(member['borrow_books']) >= 3:
            print('You cannot borrow more than 3 books')
            return False

        db = _parse_date(date_borrow)
        dr = _parse_date(date_return)
        if not db or not dr:
            return False
        if dr < db:
            print('Return date must be on/after borrow date')
            return False

        # prevent same book duplicate borrow by same member
        if any(b['book_id'] == book_id for b in member['borrow_books']):
            print('Member already has this book borrowed')
            return False

        # commit borrow
        book['count'] -= 1
        if member_id not in book['borrowers']:
            book['borrowers'].append(member_id)

        member['borrow_books'].append({
            'book_id': book_id,
            'date_borrow': db,
            'date_return': dr
        })

        history.append(f"[BORROW] {member['name']} borrowed '{book['title']}' ({db} -> {dr})")
        return True

    def return_book(book_id, member_id):
        if book_id not in BOOKS:
            print('Cannot find this book')
            return False
        if member_id not in MEMBERS:
            print('Cannot find this member')
            return False

        book = BOOKS[book_id]
        member = MEMBERS[member_id]

        # find borrow record index
        idx = next((i for i, b in enumerate(member['borrow_books']) if b['book_id'] == book_id), None)
        if idx is None:
            print('This member did not borrow this book')
            return False

        # commit return
        borrow_record = member['borrow_books'].pop(idx)
        # remove member from book.borrowers once (if present)
        if member_id in book['borrowers']:
            book['borrowers'].remove(member_id)
        book['count'] += 1

        history.append(f"[RETURN] {member['name']} returned '{book['title']}' (borrowed {borrow_record['date_borrow']} -> returned {datetime.today().date()})")
        return True

    # ---------- Search ----------
    def search_books(keyword):
        print(f"\nSearch results for books '{keyword}':")
        key = str(keyword).strip().lower()
        results = []
        for book_id, book in BOOKS.items():
            if key in book['title'].lower() or key in book['author'].lower():
                status = 'available' if _is_available(book) else 'not available'
                results.append({'id': book_id, 'title': book['title'], 'author': book['author'], 'status': status, 'count': book['count']})
                print(f"{book_id}) {book['title']} - {book['author']} - {status} ({book['count']} copies)")
        if not results:
            print("No books found.")
        return results

    def search_members(keyword):
        print(f"\nSearch results for members '{keyword}':")
        key = str(keyword).strip().lower()
        results = []
        for member_id, member in MEMBERS.items():
            if key in member['name'].lower() or key in member['email'].lower():
                results.append({'id': member_id, 'name': member['name'], 'email': member['email']})
                print(f"{member_id}) {member['name']} - {member['email']} - Borrowed: {len(member['borrow_books'])}")
        if not results:
            print("No members found.")
        return results

    # ---------- History ----------
    def show_history():
        print("\n---------------- History ---------------")
        if not history:
            print("No actions yet.")
        else:
            for line in history:
                print(line)

    # ---------- Menu (interactive) ----------
    def menu():
        while True:
            print("\n========== Library Menu ==========")
            print("1. Display Books")
            print("2. Display Members")
            print("3. Add Book")
            print("4. Add Member")
            print("5. Borrow Book")
            print("6. Return Book")
            print("7. Search Books")
            print("8. Search Members")
            print("9. Show History")
            print("0. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                display_books()
            elif choice == "2":
                display_members()
            elif choice == "3":
                title = input("Enter book title: ")
                author = input("Enter author: ")
                try:
                    count = int(input("Enter number of copies: "))
                except ValueError:
                    print("Count must be a number.")
                    continue
                add_book(title, author, count)
            elif choice == "4":
                name = input("Enter member name: ")
                email = input("Enter member email: ")
                add_member(name, email)
            elif choice == "5":
                try:
                    book_id = int(input("Enter book ID: "))
                    member_id = int(input("Enter member ID: "))
                except ValueError:
                    print("IDs must be numbers.")
                    continue
                date_borrow = input("Enter borrow date (YYYY-MM-DD): ")
                date_return = input("Enter return date (YYYY-MM-DD): ")
                borrow_book(book_id, member_id, date_borrow, date_return)
            elif choice == "6":
                try:
                    book_id = int(input("Enter book ID: "))
                    member_id = int(input("Enter member ID: "))
                except ValueError:
                    print("IDs must be numbers.")
                    continue
                return_book(book_id, member_id)
            elif choice == "7":
                keyword = input("Enter book title/author to search: ")
                search_books(keyword)
            elif choice == "8":
                keyword = input("Enter member name/email to search: ")
                search_members(keyword)
            elif choice == "9":
                show_history()
            elif choice == "0":
                print("Exiting Library System...")
                break
            else:
                print("Invalid choice. Try again.")

    # Expose API
    return {
        'menu': menu,
        'display_books': display_books,
        'display_members': display_members,
        'add_book': add_book,
        'add_member': add_member,
        'borrow_book': borrow_book,
        'return_book': return_book,
        'search_books': search_books,
        'search_members': search_members,
        'show_history': show_history,
        'BOOKS': BOOKS,
        'MEMBERS': MEMBERS,
        'history': history
    }

# ------------------ Run tests to demonstrate working behavior ------------------
lib = create_library_system()
lib['menu']()
# print("Initial books and members:")
# lib['display_books']()
# lib['display_members']()

# print("\nTry borrowing book 2 by member 101:")
# res = lib['borrow_book'](2, 101, '2025-09-01', '2025-09-15')
# print("borrow result:", res)

# print("\nState after borrow:")
# lib['display_books']()
# lib['display_members']()

# print("\nTry returning book 2 by member 101:")
# res2 = lib['return_book'](2, 101)
# print("return result:", res2)

# print("\nState after return:")
# lib['display_books']()
# lib['display_members']()

# print("\nBorrow limit test (member 102 borrows 3 books then 4th fails):")
# lib['borrow_book'](1, 102, '2025-09-01', '2025-09-10')
# lib['borrow_book'](2, 102, '2025-09-01', '2025-09-10')
# lib['borrow_book'](3, 102, '2025-09-01', '2025-09-10')
# # This one should fail (4th)
# failed = lib['borrow_book'](4, 102, '2025-09-01', '2025-09-10')
# print("4th borrow attempt (should be False):", failed)

# print("\nSearch examples:")
# lib['search_books']('py')
# lib['search_members']('sara')

# print("\nHistory log:")
# lib['show_history']()
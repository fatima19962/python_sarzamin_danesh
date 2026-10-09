def create_library_system():
    BOOKS = {
        1: {'title': 'C#', 'author': 'Erfan', 'available': True, 'borrower': [], 'count': 5},
        2: {'title': 'Java', 'author': 'Erfan', 'available': True, 'borrower': [101], 'count': 5},
        3: {'title': 'Python', 'author': 'Erfan', 'available': True, 'borrower': [], 'count': 5},
        4: {'title': 'Flutter', 'author': 'Erfan', 'available': True, 'borrower': [], 'count': 5},
    }

    MEMBERS = {
        101: {'name': 'Sara', 'email': 'test@gmail.com', 'borrow_books': [2]},
        102: {'name': 'Fatemeh', 'email': 'test@gmail.com', 'borrow_books': []},
        103: {'name': 'Maryam', 'email': 'test@gmail.com', 'borrow_books': []},
        104: {'name': 'Zahra', 'email': 'test@gmail.com', 'borrow_books': []}
    }

    history = []

    def display_books():
        print('\n---------------- Book List ----------------')
        for book_id, book in BOOKS.items():
            status = 'available' if book['available'] and book['count'] > 0 else 'not available'
            print(f"{book_id}) {book['title']} - {book['author']} - {status} - {book['count']} copies")

    def display_members():
        print('\n---------------- Member List ----------------')
        for member_id, member in MEMBERS.items():
            book_count = len(member['borrow_books'])
            print(f"{member_id}) {member['name']} - {member['email']} - {book_count} books borrowed")

    def add_book(title, author, count):
        new_id = max(BOOKS.keys()) + 1 if BOOKS else 1
        BOOKS[new_id] = {
            'title': title,
            'author': author,
            'available': True,
            'borrower': [],
            'count': count
        }
        history.append(f"Book '{title}' added to library")
        return new_id

    def add_member(name, email):
        new_id = max(MEMBERS.keys()) + 1 if MEMBERS else 101
        MEMBERS[new_id] = {'name': name, 'email': email, 'borrow_books': []}
        history.append(f"Member '{name}' added to library")
        return new_id

    def borrow_book(book_id, member_id, date_borrow, date_return):
        if book_id not in BOOKS:
            print('❌ Book not found.')
            return False
        if member_id not in MEMBERS:
            print('❌ Member not found.')
            return False
        if BOOKS[book_id]['count'] <= 0:
            print('❌ Book is currently unavailable.')
            return False
        if len(MEMBERS[member_id]['borrow_books']) >= 3:
            print('❌ Cannot borrow more than 3 books.')
            return False

        BOOKS[book_id]['count'] -= 1
        if BOOKS[book_id]['count'] == 0:
            BOOKS[book_id]['available'] = False

        BOOKS[book_id]['borrower'].append(member_id)
        BOOKS[book_id]['date_borrow'] = date_borrow
        BOOKS[book_id]['date_return'] = date_return
        MEMBERS[member_id]['borrow_books'].append(book_id)

        history.append(f"Book '{BOOKS[book_id]['title']}' borrowed by {MEMBERS[member_id]['name']}")
        return True

    def return_book(book_id):
        if book_id not in BOOKS:
            print('❌ Book not found.')
            return False
        book = BOOKS[book_id]
        if book['available']:
            print('ℹ️ Book is already available.')
            return False

        borrower_ids = book['borrower']
        for borrower_id in borrower_ids:
            if borrower_id in MEMBERS and book_id in MEMBERS[borrower_id]['borrow_books']:
                MEMBERS[borrower_id]['borrow_books'].remove(book_id)
                history.append(f"Book '{book['title']}' returned by {MEMBERS[borrower_id]['name']}")
                break

        book['count'] += 1
        book['available'] = True
        book['borrower'] = []
        return True

    def search_books(keyword):
        results = [
            (book_id, book) for book_id, book in BOOKS.items()
            if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower()
        ]
        if results:
            print('\n🔍 Book Search Results:')
            for book_id, book in results:
                status = 'available' if book['available'] and book['count'] > 0 else 'not available'
                print(f"{book_id}) {book['title']} - {book['author']} - {status}")

    def search_members(keyword):
        results = [
            (member_id, member) for member_id, member in MEMBERS.items()
            if keyword.lower() in member['name'].lower() or keyword.lower() in member['email'].lower()
        ]
        if results:
            print('\n🔍 Member Search Results:')
            for member_id, member in results:
                book_count = len(member['borrow_books'])
                print(f"{member_id}) {member['name']} - {member['email']} - {book_count} books borrowed")

    def show_history():
        print('\n📜 Transaction History:')
        for record in history:
            print(record)

    def menu():
        print('''
        📚 Library System Menu
        -----------------------
        1) Display all books
        2) Display all members
        3) Add a new book
        4) Add a new member
        5) Borrow a book
        6) Return a book
        7) Search for books
        8) Search for members
        9) Show history
        0) Exit
        ''')
        while True:
            choice = input('Enter your choice: ')
            if choice == '1':
                display_books()
            elif choice == '2':
                display_members()
            elif choice == '3':
                title = input('Enter book title: ')
                author = input('Enter book author: ')
                count = int(input('Enter book count: '))
                new_id = add_book(title, author, count)
                print(f'✅ Book added with ID: {new_id}')
            elif choice == '4':
                name = input('Enter member name: ')
                email = input('Enter member email: ')
                new_id = add_member(name, email)
                print(f'✅ Member added with ID: {new_id}')
            elif choice == '5':
                book_id = int(input('Enter book ID to borrow: '))
                member_id = int(input('Enter member ID: '))
                date_borrow = input('Enter borrow date (YYYY-MM-DD): ')
                date_return = input('Enter return date (YYYY-MM-DD): ')
                if borrow_book(book_id, member_id, date_borrow, date_return):
                    print('✅ Book borrowed successfully.')
            elif choice == '6':
                book_id = int(input('Enter book ID to return: '))
                if return_book(book_id):
                    print('✅ Book returned successfully.')
            elif choice == '7':
                keyword = input('Enter keyword to search for books: ')
                search_books(keyword)
            elif choice == '8':
                keyword = input('Enter keyword to search for members: ')
                search_members(keyword)
            elif choice == '9':
                show_history()
            elif choice == '0':
                print('👋 Exiting the system. Goodbye!')
                break
            else:
                print('❌ Invalid choice. Please try again.')

    return menu()

if __name__ == '__main__':
    library_system = create_library_system()
    library_system()

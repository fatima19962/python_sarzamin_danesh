def create_library_system():
    BOOKS = {
        1: {'title': 'C#', 'auther': 'Erfan', 'available': True, 'borrower': None, 'count': 5},
        2: {'title': 'Java', 'auther': 'Erfan', 'available': False, 'borrower': 101, 'count': 5},
        3: {'title': 'Python', 'auther': 'Erfan', 'available': True, 'borrower': None, 'count': 5},
        4: {'title': 'Flutter', 'auther': 'Erfan', 'available': True, 'borrower': None, 'count': 5},
    }

    MEMBERS = {
        101: {'name': 'Sara', 'email': 'test@gmail.com', 'borrow_books': [2]},
        102: {'name': 'Fatemeh', 'email': 'test@gmail.com', 'borrow_books': []},
        103: {'name': 'Maryam', 'email': 'test@gmail.com', 'borrow_books': []},
        104: {'name': 'Zahra', 'email': 'test@gmail.com', 'borrow_books': []}
    }

    history = []

    def display_books():
        print('\n📘--- Book List ---')
        for book_id, book in BOOKS.items():
            status = 'Available' if book['available'] and book['count'] > 0 else 'Not Available'
            print(f"{book_id}) Title: {book['title']}, Author: {book['auther']}, Status: {status}, Copies: {book['count']}")

    def display_members():
        print('\n👤--- Member List ---')
        for member_id, member in MEMBERS.items():
            borrowed_count = len(member['borrow_books'])
            print(f"{member_id}) Name: {member['name']}, Email: {member['email']}, Borrowed Books: {borrowed_count}")

    def add_book(title, auther, count):
        new_id = max(BOOKS.keys()) + 1 if BOOKS else 1
        BOOKS[new_id] = {'title': title, 'auther': auther, 'available': True, 'borrower': None, 'count': count}
        history.append(f"Book '{title}' added to library.")
        return new_id

    def add_member(name, email):
        new_id = max(MEMBERS.keys()) + 1 if MEMBERS else 101
        MEMBERS[new_id] = {'name': name, 'email': email, 'borrow_books': []}
        history.append(f"Member '{name}' added to library.")
        return new_id

    def borrow_book(book_id, member_id, date_borrow, date_return):
        if book_id not in BOOKS:
            print('❌ Book not found.')
            return False
        if member_id not in MEMBERS:
            print('❌ Member not found.')
            return False
        if not BOOKS[book_id]['available']:
            print('❌ Book is currently unavailable.')
            return False
        if len(MEMBERS[member_id]['borrow_books']) >= 3:
            print('❌ Cannot borrow more than 3 books.')
            return False

        BOOKS[book_id]['available'] = False
        BOOKS[book_id]['borrower'] = member_id
        BOOKS[book_id]['date_borrow'] = date_borrow
        BOOKS[book_id]['date_return'] = date_return
        MEMBERS[member_id]['borrow_books'].append(book_id)

        history.append(f"Book '{BOOKS[book_id]['title']}' borrowed by {MEMBERS[member_id]['name']}.")
        return True

    def return_book(book_id):
        if book_id not in BOOKS:
            print('❌ Book not found.')
            return False
        book = BOOKS[book_id]
        if book['available']:
            print('ℹ️ Book is already available.')
            return False

        member_id = book['borrower']
        if member_id in MEMBERS:
            MEMBERS[member_id]['borrow_books'].remove(book_id)
            book['available'] = True
            book['borrower'] = None
            history.append(f"Book '{book['title']}' returned by {MEMBERS[member_id]['name']}.")
            return True
        else:
            print('❌ Borrower not found.')
            return False

    def search_books(keyword):
        print('\n🔍--- Search Results: Books ---')
        keyword = keyword.lower()
        results = [
            (book_id, book) for book_id, book in BOOKS.items()
            if keyword in book['title'].lower() or keyword in book['auther'].lower()
        ]
        if results:
            for book_id, book in results:
                status = 'Available' if book['available'] and book['count'] > 0 else 'Not Available'
                print(f"{book_id}) Title: {book['title']}, Author: {book['auther']}, Status: {status}")
        else:
            print("No matching books found.")

    def search_members(keyword):
        print('\n🔍--- Search Results: Members ---')
        keyword = keyword.lower()
        results = [
            (member_id, member) for member_id, member in MEMBERS.items()
            if keyword in member['name'].lower() or keyword in member['email'].lower()
        ]
        if results:
            for member_id, member in results:
                borrowed_count = len(member['borrow_books'])
                print(f"{member_id}) Name: {member['name']}, Email: {member['email']}, Borrowed Books: {borrowed_count}")
        else:
            print("No matching members found.")

    def show_history():
        print('\n📜--- History ---')
        for record in history:
            print(record)

    def menu():
        print('''
📚 Welcome to the Library System 📚
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
                auther = input('Enter book author: ')
                count = int(input('Enter book count: '))
                new_id = add_book(title, auther, count)
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
                    print('📗 Book borrowed successfully.')
            elif choice == '6':
                book_id = int(input('Enter book ID to return: '))
                if return_book(book_id):
                    print('📘 Book returned successfully.')
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

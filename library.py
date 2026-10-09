class Book:

    def __init__(self,title,auther,isbn,count):
        self.title=title
        self.auther=auther
        self.isbn=isbn
        self.count=count
        self.is_available=True


    def borrow_book(self):
        if self.is_available:
            self.is_available=False
            return True
        return False
    
    def search_book(self,data):
        text=f'{self.title} \n {self.auther} \n {self.isbn}'
        if data in text:
            return True
        return False

    def return_book(self):
        self.is_available=True
    def __str__(self):
        return f"Title: {self.title}, Author: {self.auther}, ISBN: {self.isbn}, Count: {self.count}, Available: {'Yes' if self.is_available else 'No'}"
    

class Member:
    def __init__(self,id,name,family):
        self.id=id
        self.name=name
        self.family=family
        self.borrow_books=[]
    
    def borrow_book(self,book:Book):
        if book.borrow_book():
            self.borrow_books.append(book)
            return True
        return False

    def return_book(self,book:Book):
        if book in self.borrow_books:
            book.return_book()
            self.borrow_books.remove(book)
            return True
        return False

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Family: {self.family}, Borrowed Books: {[book.title for book in self.borrow_books]}"


class library:
      def __init__(self,name):
          self.name=name
          self.books=[]
          self.members=[]


      def add_books(self,book:Book):
          self.books.append(book)
          print(f'{book} is added')
      def add_member(self,member:Member): 
          self.members.append(member)
          print(f'{member} is added')
      def display_books(self):
          for book in self.books:
              print(book)
      def display_members(self):
          for member in self.members:
              print(member)
      def search_book_with_title(self,title):
          for book in self.books:
              if title == book.title: 
                 return book
          return None  
      def search_book(self,text_search):
          for book in self.books: 
              if book.search_book(text_search):
                  print(book)
          return None
      def search_member(self,mid):
          for member in self.members:
              if member.id == mid:
                  return member
          return None
      def get_available_books(self):
          available_books = [book for book in self.books if book.is_available]
          return available_books

def main():
    lib=library("My Library")
    text_menu="""
    1)add books
    2)add memeber
    3)display memeber
    4)search with title
    5)search book
    6)exit
"""
    while 1:
        get=int(input(text_menu))
        if get==1:
            lib.add_books(Book(input("enter book title: "),input("enter book auther: "),input("enter book isbn: "),int(input("enter book count: "))))
        elif get==2:
            mid = input("Enter member ID: ")
            name = input("Enter name: ")
            family = input("Enter family: ")
            lib.add_member(Member(mid,name,family))
        elif get==3:
            lib.display_members()
        elif  get==4:
              t = input("Enter title: ")
              result = lib.search_book_with_title(t)
              print(result if result else "Not Found")
        elif get==5:
            text = input("Enter search text: ")
            lib.search_book(text)
           
        elif get==6:
            print("exiting program...")
            break
       

if __name__=="__main__":
    main()





#class Book:      
#     def __init__(self,title,auther,isbn,count):
#         self.title = title
#         self.auther = auther
#         self.isbn = isbn
#         self.count = count
#         self.is_available = True
    
#     def borrow_book(self):
#         if self.is_available:
#             self.is_available = False
#             return True
#         return False

#     def search_book(self,data):
#         text = f'{self.title} \n {self.auther} \n {self.isbn}'
#         return data in text

#     def return_book(self):
#         self.is_available = True

#     def __str__(self):
#         return f"Title: {self.title}, Author: {self.auther}, ISBN: {self.isbn}, Count: {self.count}, Available: {'Yes' if self.is_available else 'No'}"


# class Member:
#     def __init__(self,id,name,family):
#         self.id=id
#         self.name=name
#         self.family=family
#         self.borrow_books=[]

#     def borrow_book(self,book:Book):
#         if book.borrow_book():
#             self.borrow_books.append(book)
#             return True
#         return False

#     def return_book(self,book:Book):
#         if book in self.borrow_books:
#             book.return_book()
#             self.borrow_books.remove(book)
#             return True
#         return False

#     def __str__(self):
#         return f"ID: {self.id}, Name: {self.name}, Family: {self.family}, Borrowed Books: {[book.title for book in self.borrow_books]}"


# class Library:
#     def __init__(self,name):
#         self.name=name
#         self.books=[]
#         self.members=[]

#     def add_books(self,book:Book):
#         self.books.append(book)
#         print(f'{book} is added')

#     def add_member(self,member:Member):
#         self.members.append(member)
#         print(f'{member} is added')

#     def display_books(self):
#         for book in self.books:
#             print(book)

#     def display_members(self):
#         for member in self.members:
#             print(member)

#     def search_book_with_title(self,title):
#         for book in self.books:
#             if title == book.title:
#                 return book
#         return None

#     def search_book(self,text_search):
#         for book in self.books:
#             if book.search_book(text_search):
#                 print(book)

#     def search_member(self,mid):
#         for member in self.members:
#             if member.id == mid:
#                 return member
#         return None

#     def get_available_books(self):
#         available_books = [book for book in self.books if book.is_available]
#         return available_books


# def main():
#     lib = Library("My Library")

#     text_menu = """
#     -------- MENU ----------
#     1) Add book
#     2) Add member
#     3) Display members
#     4) Display books
#     5) Search book with title
#     6) Search book (general)
#     7) Borrow a book
#     8) Return a book
#     0) Exit
#     ------------------------
#     """

#     while True:
#         choice = int(input(text_menu + "\n Enter choice: "))

#         if choice == 1:
#             title = input("Enter book title: ")
#             author = input("Enter book author: ")
#             isbn = input("Enter book ISBN: ")
#             count = int(input("Enter book count: "))
#             lib.add_books(Book(title,author,isbn,count))

#         elif choice == 2:
#             mid = input("Enter member ID: ")
#             name = input("Enter name: ")
#             family = input("Enter family: ")
#             lib.add_member(Member(mid,name,family))

#         elif choice == 3:
#             lib.display_members()

#         elif choice == 4:
#             lib.display_books()

#         elif choice == 5:
#             t = input("Enter title: ")
#             result = lib.search_book_with_title(t)
#             print(result if result else "Not Found")

#         elif choice == 6:
#             text = input("Enter search text: ")
#             lib.search_book(text)

#         elif choice == 7:
#             mid = input("Enter member ID: ")
#             member = lib.search_member(mid)
#             if not member:
#                 print("Member not found!")
#                 continue

#             title = input("Enter book title to borrow: ")
#             book = lib.search_book_with_title(title)
#             if not book:
#                 print("Book not found!")
#                 continue

#             if member.borrow_book(book):
#                 print("Book borrowed successfully!")
#             else:
#                 print("Book not available!")

#         elif choice == 8:
#             mid = input("Enter member ID: ")
#             member = lib.search_member(mid)
#             if not member:
#                 print("Member not found!")
#                 continue

#             title = input("Enter book title to return: ")
#             book = lib.search_book_with_title(title)

#             if book and member.return_book(book):
#                 print("Book returned successfully!")
#             else:
#                 print("Return failed! Check book/member.")

#         elif choice == 0:
#             print("Exiting program...")
#             break

#         else:
#             print("Invalid choice, try again!")


# if __name__ == "__main__":
#     main()
